import strawberry
from pydantic import Field, typing
from datetime import date

@strawberry.type
class Company:
    id: int
    name: typing.Optional[str] = ""
    location: typing.Optional[str] = ""
    industry: typing.Optional[str] = ""
    inception_date: typing.Optional[date] = ""

@strawberry.type
class AddCompany:
    id: int
    name: typing.Optional[str] = ""
    location: typing.Optional[str] = ""
    industry: typing.Optional[str] = ""
    inception_date: typing.Optional[date] = ""

@strawberry.type
class CompanyExists:
    message: str = "Company with this name already exists"

@strawberry.type
class CompanyNotFound:
    message: str = "Couldn't find company with the supplied id"

@strawberry.type
class CompanyNameMissing:
    message: str = "Please supply company name"

@strawberry.type
class CompanyIdMissing:
    message: str = "Please supply company id"

@strawberry.type
class CompanyDeleted:
    message: str = "Company deleted"

