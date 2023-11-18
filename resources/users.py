from pydantic import BaseModel, EmailStr, constr
from data_service import MySQLDataService

my_sql_data_service = MySQLDataService()


class UserModel(BaseModel):
    id: int
    email: EmailStr
    name: constr(max_length=255)
    school: constr(max_length=255)
    role: constr(max_length=255)
    additional_information: str


def create_user_model(data):
    if len(data) != 6:
        raise Exception("Incomparable user data length.")

    return UserModel(id=data[0], email=data[1], name=data[2], school=data[3],
                     role=data[4], additional_information=data[5])


def create_user_tuple(data):
    if len(data) != 6:
        raise Exception("Incomparable user data length.")
    data = data.dict()
    data_to_insert = (data["id"], data["email"], data["name"], data["school"],
                      data["role"], data["additional_information"])
    return data_to_insert


class UserResource:

    def __int__(self):
        self.users_table = "users"

    def get_user(self, email) -> UserModel:
        query = f"select * from {self.users_table} where email={email}"
        print("Full SQL = ", query)
        user_data = my_sql_data_service.read_single_record(query)
        user = create_user_model(user_data)
        return user

    def insert_user(self, user_data):
        user = create_user_tuple(user_data)
        query = f"insert into {self.users_table} values {str(user)}"
        my_sql_data_service.insert_single_record(query)
        return None