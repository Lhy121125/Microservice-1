import uvicorn
from fastapi import FastAPI, Response
from resources.users import UserModel, UserResource
from resources.companies import CompanyModel, CompanyResource

app = FastAPI()
users_resource = UserResource()
companies_resource = CompanyResource()


@app.get("/")
async def base():
    the_message = f"This is the AWS EC2 feature. \nWe will use it to do data-fetching:) "
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.get("/users/id", response_model=UserModel)
async def get_user(email: str):
    result = users_resource.get_user(email)
    return result


@app.post("/users", response_model=str)
async def post_user(user_data: UserModel):
    users_resource.insert_user(user_data)
    return "insert ok"


@app.put("/users")
async def put_user():
    pass


@app.delete("/users/id")
async def delete_user():
    pass


#
# @app.get("/companies/id")
# async def get_company():
#     pass
#
# @app.post("/companies")
# async def post_company():
#     pass
#
# @app.put("/companies")
# async def put_company():
#     pass
#
# @app.delete("/companies/id")
# async def delete_company():
#     pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
