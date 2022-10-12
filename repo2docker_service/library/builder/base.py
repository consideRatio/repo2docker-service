"""
The repo2docker-service web application relies on a Python API defined in the
BaseBuilder class to do the actual work.

GET / POST / DELETE     /api/v1/builds              list builds / start build / stop build
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
    image_name:
        for jupyter-repo2docker CLI's --image-name flag.
    repo:
        for jupyter-repo2docker CLI's repo command line argument.
    ref:
        for jupyter-repo2docker CLI's --ref flag.
    config:
        for jupyter-repo2docker CLI's --config flag, but not a filename,
        but JSON string. This parameter does not accept .py file
        content, only .json file content.
    """

    image_name: str
    repo: str
    ref: str | None = ""
    config: str | None = "{}"

    # TODO: Test this JSON normalization
    @validator(config, check_fields=False)
    def config_must_be_json(cls, v):
        parsed_json = json.loads(v)
        normalized_json = json.dumps(parsed_json)
        return normalized_json


class BaseBuilder(Configurable):
    @classmethod
    async def list_builds(cls):
        """
        Lists active builds.

        Returns:
            builds (list):
                A list of dictionaries with the keys "image_name", "repo",
                "ref", "config".
        """
        raise NotImplementedError()

    @classmethod
    async def start_build(cls, build: Build):
        """
        Starts a build.

        Args:
            build:
                Representing "image_name", "repo", "ref", and "config".
        """
        raise NotImplementedError()

    @classmethod
    async def stop_build(cls, image_name: str):
        """
        Stops a build.

        Args:
            image_name: identifies the build.
        """
        raise NotImplementedError()

    @classmethod
    async def generate_build_logs(cls, image_name: str):
        """
        Yields log lines from running jupyter-repo2docker.

        Args:
            image_name: identifies the build.

        Yeilds:
            Yields log lines.
        """
        raise NotImplementedError()
