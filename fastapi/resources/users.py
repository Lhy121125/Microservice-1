from pydantic import BaseModel, EmailStr, constr
from fastapi.data_service import MySQLDataService

list_fields = ["id", "email", "name", "school", "role", "additional_information"]
tup_fields = "(id, email, name, school, role, additional_information)"


class UserModel(BaseModel):
    id: int
    email: EmailStr
    name: constr(max_length=255)
    school: constr(max_length=255)
    role: constr(max_length=255)
    additional_information: str

    @classmethod
    def create_user_model(cls, data):
        if len(data) != len(list_fields):
            return None
        else:
            return cls(
                id=data[0],
                email=data[1],
                name=data[2],
                school=data[3],
                role=data[4],
                additional_information=data[5],
            )

    @classmethod
    def create_user_tuple(cls, data):
        data = data.dict()
        data_to_insert = (
            data["id"],
            data["email"],
            data["name"],
            data["school"],
            data["role"],
            data["additional_information"],
        )
        return data_to_insert


class UserResource:
    def __init__(self):
        self.my_sql_data_service = MySQLDataService()
        self.table = "users"

    def get_user(self, id) -> UserModel:
        query = f"SELECT * FROM {self.table} WHERE ID= {id}"
        print("Full SQL = ", query)
        user_data = self.my_sql_data_service.read_single_record(query)
        user = UserModel.create_user_model(user_data)
        return user

    def post_user(self, user_data):
        user = UserModel.create_user_tuple(user_data)
        query = f"INSERT INTO {self.table} {str(tup_fields)} " f"VALUES {str(user)}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def put_user(self, user_data):
        user_data_new = user_data.model_dump()
        id = user_data_new["id"]
        user_data_old = self.get_user(id)

        # handle the cause when user is not found
        if user_data_old is None:
            return
        else:
            user_data_old = user_data_old.model_dump()

        changes = []
        for f in list_fields:
            if user_data_new[f] != user_data_old[f]:
                changes.append(f"{f} = '{user_data_new[f]}'")

        query = f"UPDATE {self.table} SET {', '.join(changes)} WHERE id = {id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def delete_user(self, id):
        query = f"DELETE FROM {self.table} WHERE ID = {id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)
