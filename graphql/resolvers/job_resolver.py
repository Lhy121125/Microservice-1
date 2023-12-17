from sqlalchemy import delete, insert, select
from sqlalchemy.orm import subqueryload,load_only

from dbsession import get_session
from helper import get_only_selected_fields, get_valid_data
from models import job_model
from scalars.job_scalar import AddJob, Job, JobDeleted, JobExists, JobNotFound


async def get_jobs(info):
    """ Get all jobs resolver """
    selected_fields = get_only_selected_fields(job_model.Job,info)
    async with get_session() as s:
        sql = select(job_model.Job).options(load_only(*selected_fields)).options(subqueryload(job_model.Job.company)) \
        .order_by(job_model.Job.job_title)
        db_jobs = (await s.execute(sql)).scalars().unique().all()

    jobs_data_list = []
    for job in db_jobs:
        job_dict = get_valid_data(job,job_model.Job)
        job_dict["company"] = job.company
        jobs_data_list.append(Job(**job_dict))

    return jobs_data_list

async def get_job(id, company_id, info):
    """ Get specific job by id resolver """
    selected_fields = get_only_selected_fields(job_model.Job,info)
    async with get_session() as s:
        sql = select(job_model.Job).options(load_only(*selected_fields)) \
        .filter(job_model.Job.id == id and job_model.Job.company_id == company_id).options(subqueryload(job_model.Job.company)) \
        .order_by(job_model.Job.job_title)
        db_job = (await s.execute(sql)).scalars().unique().one()
    
    job_dict = get_valid_data(db_job,job_model.Job)
    job_dict["company"] = db_job.company
    return Job(**job_dict)

async def delete_job(job_id):
    """ Delete job resolver """
    async with get_session() as s:
        sql = select(job_model.Job).where(job_model.Job.id == job_id)
        existing_db_job = (await s.execute(sql)).first()
        if existing_db_job is None:
            return JobNotFound()

        query = delete(job_model.Job).where(job_model.Job.id == job_id)
        await s.execute(query)
        await s.commit()
    
    return JobDeleted()