"""
The repo2docker-service web application relies on a Python API defined in the
BaseRegistry class to do the actual work. The purpose of a Registry
implementation is to list and delete images wherever they are accessed.

GET / DELETE     /api/v1/images              list images / delete image

A Builder class also needs a Registry class to upload to.

Related code:
  - jupyterhub/binderhub has a DockerRegistry class, see:
      - https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/registry.py#L18
  - plasmabio/tljh-repo2docker has a list_images function to inspect the local
    docker daemon, see:
      - https://github.com/plasmabio/tljh-repo2docker/blob/d711bda82942d55eb14395993c1d63043294fae8/tljh_repo2docker/docker.py#L8
"""


class BaseRegistry:
    pass
