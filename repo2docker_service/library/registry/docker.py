"""
An external Docker registry has a _catalog_ of _repositories_ containing
different _tags_ of an image. A Docker Registry's v2 REST API can be used to get
a catalog.

- https://docs.docker.com/registry/spec/api/#listing-repositories

If we use a public Docker registry, we must be able to paginate repositories in
our control and not all repositories though.

> Note that the contents of the response are specific to the registry
  implementation. Some registries may opt to provide a full catalog output,
  limit it based on the user’s access level or omit upstream results, if
  providing mirroring functionality.

That makes this implementation a tricky and not so robust.

---

At the time of writing, the following libraries and code snippets have been
considered to help us out:

- https://github.com/davedoesdev/dxf

  It is not async.

- https://github.com/crashvb/docker-registry-client-async

  It is a small project not widely used or actively developed.

- https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/registry.py#L18

  It can get you a single image manifest, not a full catalog.
"""

from .base import Registry


class DockerRegistry(Registry):
    @classmethod
    async def list_images(cls):
        """
        Lists built images.

        Example response:

            []
        """
        raise NotImplementedError()
