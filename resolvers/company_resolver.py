from sqlalchemy import delete, insert, select
from sqlalchemy.orm import subqueryload,load_only

from dbsession import get_session
from helper import get_only_selected_fields, get_valid_data
from models import company_model
from scalars.company_scalar import AddCompany, Company, CompanyDeleted, CompanyExists, CompanyNotFound


async def get_companies(info):
    """ Get all companies resolver """
    selected_fields = get_only_selected_fields(company_model.Company,info)
    async with get_session() as s:
        sql = select(company_model.Company).options(load_only(*selected_fields)) \
        .order_by(company_model.Company.name)
        db_companies = (await s.execute(sql)).scalars().unique().all()

    companies_data_list = []
    for company in db_companies:
        company_dict = get_valid_data(company,company_model.Company)
        companies_data_list.append(Company(**company_dict))

    return companies_data_list

async def get_company(company_id, info):
    """ Get specific company by id resolver """
    selected_fields = get_only_selected_fields(company_model.Company,info)
    async with get_session() as s:
        sql = select(company_model.Company).options(load_only(*selected_fields)) \
        .filter(company_model.Company.id == company_id).order_by(company_model.Company.name)
        db_company = (await s.execute(sql)).scalars().unique().one()
    
    company_dict = get_valid_data(db_company,company_model.Company)
    return Company(**company_dict)