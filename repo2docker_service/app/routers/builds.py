from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ...library.builder import Build, MockedBuilder

router = APIRouter(
    prefix="/builds",
    tags=["builds"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_builds():
    return await MockedBuilder.list_builds()


@router.post("/")
async def start_build(build: Build):
    return await MockedBuilder.start_build(build)


@router.delete("/{image_name}")
async def stop_build(image_name):
    return await MockedBuilder.stop_build(image_name)


# FIXME: handle image_name containing / etc.
@router.get("/{image_name}/logs")
async def generate_build_logs(image_name):
    return StreamingResponse(MockedBuilder.generate_build_logs(image_name))
