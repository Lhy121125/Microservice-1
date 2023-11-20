from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import List


class CompanyModel(BaseModel):
    id: int
    name: constr(max_length=255)
    location: constr(max_length=255)
    industry: constr(max_length=255)
    inception_date: date


class CompanyResource:
    def __int__(self):
        self.companies = None

    def get_company(self) -> List[CompanyModel]:
        return self.companies
