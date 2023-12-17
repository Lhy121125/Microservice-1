import strawberry
from pydantic import Field, typing
from datetime import date
from scalars.job_scalar import Job
from scalars.user_scalar import User

@strawberry.type
class Application:
    company_id: int
    job_id: int
    user_id: int
    time_applied: typing.Optional[date]
    application_status: typing.Optional[str]
    job: typing.Optional[typing.List[Job]] = Field(default_factory=list)
    user: typing.Optional[typing.List[User]] = Field(default_factory=list)

@strawberry.type
class AddApplication:
    company_id: int
    job_id: int
    user_id: int
    time_applied: typing.Optional[date]
    application_status: typing.Optional[str]
    
@strawberry.type
class ApplicationExists:
    message: str = "Application with this name already exists"

@strawberry.type
class ApplicationNotFound:
    message: str = "Couldn't find Application with the supplied id"

@strawberry.type
class ApplicationNameMissing:
    message: str = "Please supply Application name"

@strawberry.type
class ApplicationIdMissing:
    message: str = "Please supply Application id"

@strawberry.type
class ApplicationDeleted:
    message: str = "Application deleted"