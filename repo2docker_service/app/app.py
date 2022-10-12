"""
A reference example on how to write this code is available at:
https://github.com/jupyterhub/jupyterhub/blob/main/examples/service-fastapi/app/app.py
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .._version import __version__
from .routers import builds

app = FastAPI(
    title="Repo2Docker Service",
    version=__version__,
)
app.include_router(builds.router)
app.mount(
    "/", StaticFiles(packages=[("repo2docker_service", "frontend/build")], html=True)
)
