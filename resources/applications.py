from pydantic import BaseModel
from data_service import MySQLDataService
from datetime import date

list_fields = ["company_id", "job_id", "user_id", "time_applied", "application_status"]
tup_fields = "(company_id, job_id, user_id, time_applied, application_status)"


class ApplicationModel(BaseModel):
    company_id: int
    job_id: int
    user_id: int
    time_applied: date
    application_status: str

    @classmethod
    def create_application_model(cls, data):
        if len(data) != len(list_fields):
            return None
        else:
            return cls(
                company_id=data[0],
                job_id=data[1],
                user_id=data[2],
                time_applied=data[3],
                application_status=data[4],
            )

    @classmethod
    def create_application_tuple(cls, data):
        data = data.dict()
        data_to_insert = (
            data["company_id"],
            data["job_id"],
            data["user_id"],
            data["time_applied"].strftime("%Y-%m-%d %H:%M:%S"),
            data["application_status"],
        )
        return data_to_insert


class ApplicationResource:
    def __init__(self):
        self.my_sql_data_service = MySQLDataService()
        self.table = "applications"

    def get_application(self, company_id, job_id, user_id) -> ApplicationModel:
        query = f"SELECT * FROM {self.table} WHERE company_id = {company_id} AND job_id = {job_id} AND user_id = {user_id}"
        print("Full SQL = ", query)
        data = self.my_sql_data_service.read_single_record(query)
        application = ApplicationModel.create_application_model(data)
        return application

    def get_all_applications(self, user_id):
        query = f"SELECT * FROM {self.table} WHERE user_id = {user_id}"
        print("Full SQL = ", query)
        data = self.my_sql_data_service.read_all_records(query)
        applications = []
        for line in data:
            applications.append(ApplicationModel.create_application_model(line))
        return applications

    def post_application(self, data):
        application = ApplicationModel.create_application_tuple(data)
        query = (
            f"INSERT INTO {self.table} {str(tup_fields)} " f"VALUES {str(application)}"
        )
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def put_application(self, data):
        data_new = data.model_dump()
        company_id, job_id, user_id = (
            data_new["company_id"],
            data_new["job_id"],
            data_new["user_id"],
        )
        data_old = self.get_application(company_id, job_id, user_id)
        if data_old is None:
            return
        else:
            data_old = data_old.model_dump()

        changes = []
        for f in list_fields:
            if data_new[f] != data_old[f]:
                changes.append(f"{f} = '{data_new[f]}'")

        query = f"UPDATE {self.table} SET {', '.join(changes)} WHERE company_id = {company_id} AND job_id = {job_id} AND user_id = {user_id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def delete_application(self, company_id, job_id, user_id):
        query = f"DELETE FROM {self.table} WHERE company_id = {company_id} AND job_id = {job_id} AND user_id = {user_id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)
