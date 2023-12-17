import strawberry
from pydantic import typing
from strawberry.types import Info
from resolvers.user_resolver import get_user, get_users, delete_user
from scalars.user_scalar import User
from fragments.user_fragments import AddUserResponse, DeleteUserResponse
from resolvers.company_resolver import get_company, get_companies
from scalars.company_scalar import Company
from fragments.company_fragments import AddCompanyResponse, DeleteCompanyResponse

@strawberry.type
class Query:

    @strawberry.field
    async def users(self, info:Info) -> typing.List[User]:
        """ Get all users """
        users_data_list = await get_users(info)
        return users_data_list

    @strawberry.field
    async def user(self, info:Info, user_id: int) -> User:
        """ Get user by id """
        user_dict = await get_user(user_id, info)
        return user_dict
    
    @strawberry.field
    async def companies(self, info:Info) -> typing.List[Company]:
        """ Get all companies """
        companies_data_list = await get_companies(info)
        return companies_data_list

    @strawberry.field
    async def company(self, info:Info, company_id: int) -> Company:
        """ Get company by id """
        company_dict = await get_company(company_id, info)
        return company_dict


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def delete_user(self, user_id: int) -> DeleteUserResponse:
        """ Delete user """
        delete_user_resp = await delete_user(user_id)
        return delete_user_resp