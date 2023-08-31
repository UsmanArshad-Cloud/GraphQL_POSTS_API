from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import final_schema

app = FastAPI()
graphql_app = GraphQLRouter(final_schema)
app.include_router(graphql_app, prefix="/graphql")
