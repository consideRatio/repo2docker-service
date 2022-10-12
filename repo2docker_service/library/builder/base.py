"""
The repo2docker-service web application relies on a Python API defined in the
Builder class to do the actual work, see app/routers/builds.py.

GET                     /api/v1/builds              list builds
POST                    /api/v1/builds              start build
DELETE                  /api/v1/builds/{id}         stop build
GET                     /api/v1/builds/{id}/logs    stream logs from build

Related code:
  - jupyterhub/binderhub has a BuildExecutor class and a KubernetesBuildExecutor
    class, see:
      - https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/build.py#L56
      - https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/build.py#L189
  - plasmabio/tljh-repo2docker has list_containers and build_image functions,
    that maps to list_builds and start_build here, as well as logic to get logs
    from a build container, see:
      - https://github.com/plasmabio/tljh-repo2docker/blob/d711bda82942d55eb14395993c1d63043294fae8/tljh_repo2docker/docker.py
      - https://github.com/plasmabio/tljh-repo2docker/blob/d711bda82942d55eb14395993c1d63043294fae8/tljh_repo2docker/logs.py#L21-L32
"""
import json

from pydantic import BaseModel, validator
from traitlets.config.configurable import Configurable


class Build(BaseModel):
    """
    Represents a Build

    id:
        provided by the builder
    image_name:
        for jupyter-repo2docker CLI's --image-name flag.
    repo:
        for jupyter-repo2docker CLI's repo command line argument.
    ref:
        for jupyter-repo2docker CLI's --ref flag.
    config:
        for jupyter-repo2docker CLI's --config flag, but not a filename, but
        JSON string. This parameter does not accept .py file content, only .json
        file content.
    """

    id: str | None = None
    image_name: str
    repo: str
    ref: str | None = ""
    config: str | None = "{}"

    # TODO: Test this JSON normalization
    # TODO: Conclude if this should error without handling or not
    @validator(config, check_fields=False)
    def normalize_config(cls, v):
        parsed_json = json.loads(v)
        normalized_json = json.dumps(parsed_json)
        return normalized_json


class Builder(Configurable):
    @classmethod
    async def list_builds(cls):
        """
        Lists active builds.
        """
        raise NotImplementedError()

    @classmethod
    async def start_build(cls, build: Build):
        """
        Starts a build.
        """
        raise NotImplementedError()

    @classmethod
    async def stop_build(cls, image_name: str):
        """
        Stops a build.
        """
        raise NotImplementedError()

    @classmethod
    async def generate_build_logs(cls, image_name: str):
        """
        Yields log lines from running jupyter-repo2docker.

        Yeilds:
            Yields log lines.
        """
        raise NotImplementedError()
