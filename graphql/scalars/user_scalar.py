import strawberry
from pydantic import Field, typing

@strawberry.type
class User:
    id: int
    email: typing.Optional[str] = ""
    name: typing.Optional[str] = ""
    school: typing.Optional[str] = ""
    role: typing.Optional[str] = ""
    additional_information: typing.Optional[str] = ""

@strawberry.type
class AddUser:
    id: int
    email: typing.Optional[str] = ""
    name: typing.Optional[str] = ""
    school: typing.Optional[str] = ""
    role: typing.Optional[str] = ""
    additional_information: typing.Optional[str] = ""

@strawberry.type
class UserExists:
    message: str = "User with this name already exists"

@strawberry.type
class UserNotFound:
    message: str = "Couldn't find user with the supplied id"

@strawberry.type
class UserNameMissing:
    message: str = "Please supply user name"

@strawberry.type
class UserIdMissing:
    message: str = "Please supply user id"

@strawberry.type
class UserDeleted:
    message: str = "User deleted"