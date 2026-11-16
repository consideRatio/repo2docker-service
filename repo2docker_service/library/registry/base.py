"""
The repo2docker-service web application relies on a Python API defined in the
Registry class to do the actual work. The purpose of a Registry
implementation is to list and delete images from where images can end up.

GET     /api/v1/images              list images
DELETE  /api/v1/images/:image_name  delete image

Related code:
  - jupyterhub/binderhub has a DockerRegistry class, see:
      - https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/registry.py#L18
  - plasmabio/tljh-repo2docker has a list_images function to inspect the local
    docker daemon, see:
      - https://github.com/plasmabio/tljh-repo2docker/blob/d711bda82942d55eb14395993c1d63043294fae8/tljh_repo2docker/docker.py#L8
"""

from traitlets.config.configurable import Configurable


class Registry(Configurable):
    @classmethod
    async def list_images(cls):
        """
        Lists built images.
        """
        raise NotImplementedError()
