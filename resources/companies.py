from pydantic import BaseModel, EmailStr, constr
from data_service import MySQLDataService
from datetime import date
from time import strftime, strptime

list_fields = ["id", "name", "location", "industry", "inception_date"]
tup_fields = "(id, name, location, industry, inception_date)"


class CompanyModel(BaseModel):
    id: int
    name: constr(max_length=255)
    location: constr(max_length=255)
    industry: constr(max_length=255)
    inception_date: date

    @classmethod
    def create_company_model(cls, data):
        if len(data) != len(list_fields):
            return None
        else:
            return cls(
                id=data[0],
                name=data[1],
                location=data[2],
                industry=data[3],
                inception_date=data[4],
            )

    @classmethod
    def create_company_tuple(cls, data):
        data = data.dict()
        data_to_insert = (
            data["id"],
            data["name"],
            data["location"],
            data["industry"],
            data["inception_date"].strftime("%Y-%m-%d %H:%M:%S"),
        )
        return data_to_insert


class CompanyResource:
    def __init__(self):
        self.my_sql_data_service = MySQLDataService()
        self.table = "companies"

    def get_company(self, id) -> CompanyModel:
        query = f"SELECT * FROM {self.table} WHERE id = {id}"
        print("Full SQL = ", query)
        company_data = self.my_sql_data_service.read_single_record(query)
        company = CompanyModel.create_company_model(company_data)
        return company

    def post_company(self, company_data):
        company = CompanyModel.create_company_tuple(company_data)
        query = f"INSERT INTO {self.table} {str(tup_fields)} VALUES {str(company)}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def put_company(self, company_data):
        company = company_data.model_dump()
        id = company["id"]
        existing_company = self.get_company(id)

        if existing_company is None:
            return
        else:
            existing_company = existing_company.model_dump()

        changes = []
        for field in list_fields:
            if company[field] != existing_company[field]:
                changes.append(f"{field} = '{company[field]}'")

        query = f"UPDATE {self.table} SET {', '.join(changes)} WHERE id = {id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)

    def delete_company(self, id):
        query = f"DELETE FROM {self.table} WHERE id = {id}"
        print("Full SQL = ", query)
        self.my_sql_data_service.write_single_record(query)
