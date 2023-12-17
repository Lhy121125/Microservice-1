import strawberry
from pydantic import Field, typing

@strawberry.type
class Job:
    id: int
    company_id: int
    job_title: typing.Optional[str] = ""
    department: typing.Optional[str] = ""
    location: typing.Optional[str] = ""
    employment_type: typing.Optional[str] = ""
    description: typing.Optional[str] = ""
    requirements: typing.Optional[str] = ""

@strawberry.type
class AddJob:
    id: int
    company_id: int
    job_title: typing.Optional[str] = ""
    department: typing.Optional[str] = ""
    location: typing.Optional[str] = ""
    employment_type: typing.Optional[str] = ""
    description: typing.Optional[str] = ""
    requirements: typing.Optional[str] = ""
    
@strawberry.type
class JobExists:
    message: str = "Job with this name already exists"

@strawberry.type
class JobNotFound:
    message: str = "Couldn't find Job with the supplied id"

@strawberry.type
class JobNameMissing:
    message: str = "Please supply Job name"

@strawberry.type
class JobIdMissing:
    message: str = "Please supply Job id"

@strawberry.type
class JobDeleted:
    message: str = "Job deleted"