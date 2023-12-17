import strawberry
from scalars.company_scalar import AddCompany, CompanyDeleted, CompanyExists, CompanyIdMissing, CompanyNotFound


AddCompanyResponse = strawberry.union("AddCompanyResponse", (AddCompany, CompanyExists))
DeleteCompanyResponse = strawberry.union("DeleteCompanyResponse", (CompanyDeleted,CompanyNotFound, CompanyIdMissing))