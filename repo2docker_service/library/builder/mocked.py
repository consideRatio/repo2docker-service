"""
The MockedBuilder is meant to mock actually building something.

Related code:
  - jupyterhub/binderhub has a FakeBuild class, see:
      - https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/build.py#L670
"""
import asyncio

from .base import BaseBuilder, Build

db = [
    Build(
        repo="https://github.com/binderhub-ci-repos/cached-minimal-dockerfile",
        ref="main",
        image_name="binderhub-ci-repos/cached-minimal-dockerfile:main",
        config="{}",
    ),
]


class MockedBuilder(BaseBuilder):
    @classmethod
    async def list_builds(cls):
        return db

    @classmethod
    async def start_build(cls, build: Build):
        await asyncio.sleep(1)
        db.append(build)
        return

    @classmethod
    async def stop_build(cls, image_name: str):
        build = cls._get_build(image_name)
        if build:
            await asyncio.sleep(1)
            db.remove(build)
        return

    @classmethod
    async def generate_build_logs(cls, image_name: str):
        build = cls._get_build(image_name)
        if build:
            yield "mocked log line 1"
            await asyncio.sleep(1)
            yield "mocked log line 2"
            await asyncio.sleep(1)
            yield "mocked log line 3"

    @classmethod
    def _get_build(cls, image_name):
        return next((b for b in db if b.image_name == image_name), None)
