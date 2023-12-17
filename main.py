import uvicorn
from fastapi import FastAPI, Response
from resources.users import UserModel, UserResource
from resources.companies import CompanyModel, CompanyResource
from resources.applications import ApplicationModel, ApplicationResource
from resources.jobs import JobModel, JobResource
import requests

app = FastAPI(debug=True)
users_resource = UserResource()
companies_resource = CompanyResource()
applications_resource = ApplicationResource()
jobs_resource = JobResource()
email_api = "insert your email api here"

@app.get("/")
async def base():
    the_message = (
        f"This is the AWS EC2 feature. \nWe will use it to do data-fetching:) "
    )
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.get("/users/{id}", response_model=None)
async def get_user(id: int, page: int = 1, page_size: int = 1):
    result = users_resource.get_user(id, page, page_size)
    return result


@app.post("/users", response_model=str)
async def post_user(user_data: UserModel):
    users_resource.post_user(user_data)
    return "insert ok"


@app.put("/users", response_model=str)
async def put_user(user_data: UserModel):
    users_resource.put_user(user_data)
    return "update ok"


@app.delete("/users", response_model=str)
async def delete_user(id: int):
    users_resource.delete_user(id)
    return "delete ok"


@app.get("/companies/{id}", response_model=None)
async def get_company(id: int):
    result = companies_resource.get_company(id)
    return result


@app.post("/companies", response_model=str)
async def post_company(data: CompanyModel):
    companies_resource.post_company(data)
    return "insert ok"


@app.put("/companies", response_model=str)
async def put_company(data: CompanyModel):
    companies_resource.put_company(data)
    return "update ok"


@app.delete("/companies", response_model=str)
async def delete_company(id: int):
    companies_resource.delete_company(id)
    return "delete ok"


@app.get("/jobs", response_model=None)
async def get_job(id: int, company_id: int):
    result = jobs_resource.get_job(id, company_id)
    return result

@app.get("/jobs_all", response_model=None)
async def get_all_jobs(page: int = 1, page_size: int = 1):
    result = jobs_resource.get_all_jobs(page, page_size)
    return result

@app.post("/jobs", response_model=str)
async def post_job(data: JobModel):
    jobs_resource.post_job(data)
    return "insert ok"


@app.put("/jobs", response_model=str)
async def put_job(data: JobModel):
    jobs_resource.put_job(data)
    return "update ok"


@app.delete("/jobs", response_model=str)
async def delete_job(id: int, company_id: int):
    jobs_resource.delete_job(id, company_id)
    return "delete ok"


@app.get("/applications", response_model=None)
async def get_application(
    company_id: int, job_id: int, user_id: int
):
    result = applications_resource.get_application(company_id, job_id, user_id)
    return result

@app.get("/applications/{id}", response_model=None)
async def get_application(id:int):
    result = applications_resource.get_all_applications(id)
    return result


@app.post("/applications", response_model=str)
async def post_application(data: ApplicationModel):
    applications_resource.post_application(data)
    return "insert ok"


@app.put("/applications", response_model=str)
async def put_application(data: ApplicationModel):
    applications_resource.put_application(data)
    return "update ok"


@app.delete("/applications", response_model=str)
async def delete_application(company_id: int, job_id: int, user_id: int):
    applications_resource.delete_application(company_id, job_id, user_id)
    user = users_resource.get_user(user_id)
    email = user.email
    to_send = {
        "to": email,
        "subject": "ApplicationHub - notification",
        "body": "You have just deleted an application."
    }
    requests.post(email_api, json=to_send)
    return "delete ok"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
