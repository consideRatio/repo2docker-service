from fastapi import FastAPI

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
from .routers import builds

# ref: https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-apirouter
app = FastAPI()
app.include_router(builds.router)


@app.get("/")
async def root():
    return {"msg": "Hello World"}
