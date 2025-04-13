import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema  # Import the schema from the schema.py file

# Create GraphQL router using the schema
graphql_app = GraphQLRouter(schema)

# Initialize FastAPI app
app = FastAPI()

# Include the GraphQL router with the prefix '/graphql'
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
