import uvicorn
from fastapi import FastAPI, Response
from resources.users import UserModel, UserResource
from resources.companies import CompanyModel, CompanyResource

app = FastAPI(debug=True)
users_resource = UserResource()
companies_resource = CompanyResource()


@app.get("/")
async def base():
    the_message = (
        f"This is the AWS EC2 feature. \nWe will use it to do data-fetching:) "
    )
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.get("/users", response_model=None)
async def get_user(id: int) -> UserModel | None:
    result = users_resource.get_user(id)
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


@app.get("/companies", response_model=None)
async def get_company(id: int) -> CompanyModel | None:
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
