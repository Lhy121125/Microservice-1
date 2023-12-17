from fastapi import FastAPI, Response
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from schemas import Mutation
from schemas import Query
import uvicorn

schema = strawberry.Schema(query=Query,mutation=Mutation,config=StrawberryConfig(auto_camel_case=True))

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def base():
    the_message = (
        f"Enter the graphql interface through http://0.0.0.0:8012/graphql."
    )
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
