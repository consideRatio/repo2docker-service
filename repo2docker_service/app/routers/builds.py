from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ...library.builder import Build
from ..config import config

router = APIRouter(
    prefix="/builds",
    tags=["builds"],
    dependencies=[],
    responses={},
)


@router.get("/")
async def list_builds():
    return await config.builder_class.list_builds()


@router.post("/")
async def start_build(build: Build):
    return await config.builder_class.start_build(build)


@router.delete("/{id}")
async def stop_build(id):
    return await config.builder_class.stop_build(id)


@router.get("/{id}/logs")
async def generate_build_logs(id):
    return StreamingResponse(config.builder_class.generate_build_logs(id))
