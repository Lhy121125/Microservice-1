from pydantic import BaseModel, EmailStr, constr
from data_service import MySQLDataService

list_fields = [
    "id",
    "company_id",
    "job_title",
    "department",
    "location",
    "employment_type",
    "description",
    "requirements",
]
tup_fields = "(id, company_id, job_title, department, location, employment_type, description, requirements)"


class JobModel(BaseModel):
    id: int
    company_id: int
    job_title: constr(max_length=255)
    department: constr(max_length=255)
    location: constr(max_length=255)
    employment_type: constr(max_length=255)
    description: str
    requirements: str

    @classmethod
    def create_job_model(cls, data):
        if len(data) != len(list_fields):
            return None
        else:
            return cls(
                id=data[0],
                company_id=data[1],
                job_title=data[2],
                department=data[3],
                location=data[4],
                employment_type=data[5],
                description=data[6],
                requirements=data[7],
            )

    @classmethod
    def create_job_tuple(cls, data):
        data = data.dict()
        data_to_insert = (
            data["id"],
            data["company_id"],
            data["job_title"],
            data["department"],
            data["location"],
            data["employment_type"],
            data["description"],
            data["requirements"],
        )
        return data_to_insert


class JobResource:
    def __init__(self):
        self.my_sql_data_service = MySQLDataService()
        self.table = "jobs"

    def get_job(self, id, company_id) -> JobModel:
        query = (
            f"SELECT * FROM {self.table} WHERE id = {id} AND company_id = {company_id}"
        )
        print("Full SQL = ", query)
        data = self.my_sql_data_service.read_single_record(query)
        job = JobModel.create_job_model(data)
        return job

    def post_job(self, data):
        job = JobModel.create_job_tuple(data)
        query = f"INSERT INTO {self.table} {str(tup_fields)} " f"VALUES {str(job)}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def put_job(self, data):
        data_new = data.model_dump()
        id, company_id = (
            data_new["id"],
            data_new["company_id"],
        )
        data_old = self.get_job(id, company_id)
        if data_old is None:
            print(f"Job where id = {id} and company_id = {company_id} not found.")
            return
        else:
            data_old = data_old.model_dump()

        changes = []
        for f in list_fields:
            if data_new[f] != data_old[f]:
                changes.append(f"{f} = '{data_new[f]}'")

        query = f"UPDATE {self.table} SET {', '.join(changes)} WHERE id = {id} AND company_id = {company_id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def delete_job(self, id, company_id):
        query = (
            f"DELETE FROM {self.table} WHERE id = {id} AND company_id = {company_id}"
        )
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)
