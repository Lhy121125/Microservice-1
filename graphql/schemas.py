import strawberry
from pydantic import typing
from strawberry.types import Info

from resolvers.user_resolver import get_user, get_users, delete_user
from scalars.user_scalar import User
from fragments.user_fragments import AddUserResponse, DeleteUserResponse

from resolvers.company_resolver import get_company, get_companies
from scalars.company_scalar import Company
from fragments.company_fragments import AddCompanyResponse, DeleteCompanyResponse

from resolvers.job_resolver import get_job, get_jobs
from scalars.job_scalar import Job
from fragments.job_fragments import AddJobResponse, DeleteJobResponse

from resolvers.application_resolver import get_application, get_applications
from scalars.application_scalar import Application
from fragments.application_fragments import AddApplicationResponse, DeleteApplicationResponse

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
    
    @strawberry.field
    async def jobs(self, info:Info) -> typing.List[Job]:
        """ Get all jobs """
        jobs_data_list = await get_jobs(info)
        return jobs_data_list

    @strawberry.field
    async def job(self, info:Info, id: int, company_id: int) -> Job:
        """ Get job by id """
        job_dict = await get_job(id, company_id, info)
        return job_dict

    @strawberry.field
    async def applications(self, info:Info) -> typing.List[Application]:
        """ Get all applications """
        applications_data_list = await get_applications(info)
        return applications_data_list

    @strawberry.field
    async def application(self, info:Info, application_id: int, company_id: int, user_id: int) -> Application:
        """ Get application by id """
        application_dict = await get_application(application_id, company_id, user_id, info)
        return application_dict


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def delete_user(self, user_id: int) -> DeleteUserResponse:
        """ Delete user """
        delete_user_resp = await delete_user(user_id)
        return delete_user_resp