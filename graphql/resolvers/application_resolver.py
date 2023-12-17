from sqlalchemy import delete, insert, select
from sqlalchemy.orm import subqueryload,load_only

from dbsession import get_session
from helper import get_only_selected_fields, get_valid_data
from models import application_model
from scalars.application_scalar import AddApplication, Application, ApplicationDeleted, ApplicationExists, ApplicationNotFound


async def get_applications(info):
    """ Get all applications resolver """
    selected_fields = get_only_selected_fields(application_model.Application,info)
    async with get_session() as s:
        sql = select(application_model.Application).options(load_only(*selected_fields)) \
        .order_by(application_model.Application.user_id)
        db_applications = (await s.execute(sql)).scalars().unique().all()

    applications_data_list = []
    for application in db_applications:
        application_dict = get_valid_data(application,application_model.Application)
        applications_data_list.append(Application(**application_dict))

    return applications_data_list

async def get_application(user_id, job_id, company_id, info):
    """ Get specific application by id resolver """
    selected_fields = get_only_selected_fields(application_model.Application,info)
    async with get_session() as s:
        sql = select(application_model.Application).options(load_only(*selected_fields)) \
        .filter(application_model.Application.user_id == user_id and application_model.Application.job_id == job_id and application_model.Application.company_id == company_id) \
        .order_by(application_model.Application.user_id)
        db_application = (await s.execute(sql)).scalars().unique().one()
    
    application_dict = get_valid_data(db_application,application_model.Application)
    return Application(**application_dict)

# async def delete_application(application_id):
#     """ Delete application resolver """
#     async with get_session() as s:
#         sql = select(application_model.Application).where(application_model.Application.id == application_id)
#         existing_db_application = (await s.execute(sql)).first()
#         if existing_db_application is None:
#             return ApplicationNotFound()

#         query = delete(application_model.Application).where(application_model.Application.id == application_id)
#         await s.execute(query)
#         await s.commit()
    
#     return ApplicationDeleted()