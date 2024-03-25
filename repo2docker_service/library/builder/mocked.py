"""
The MockedBuilder is meant to mock actually building something.

Related code:
  - jupyterhub/binderhub has a FakeBuild class, see:
      - https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/build.py#L670
"""

import asyncio
import uuid

from .base import Build, Builder

build_db = []


class MockedBuilder(Builder):
    @classmethod
    async def list_builds(cls):
        return build_db

    @classmethod
    async def start_build(cls, build: Build):
        await asyncio.sleep(1)
        build.id = str(uuid.uuid4())
        build_db.append(build)
        return build.id

    @classmethod
    async def stop_build(cls, id: str):
        build = cls._get_build(id)
        if build:
            await asyncio.sleep(1)
            build_db.remove(build)
        return

    @classmethod
    async def generate_build_logs(cls, id: str):
        build = cls._get_build(id)
        if build:
            yield "mocked log line 1"
            await asyncio.sleep(1)
            yield "mocked log line 2"
            await asyncio.sleep(1)
            yield "mocked log line 3"

    @classmethod
    def _get_build(cls, id):
        return next((b for b in build_db if b.id == id), None)
