import json

from aiodocker import Docker

from .base import Registry


class DockerDaemonRegistry(Registry):
    @classmethod
    async def list_images(cls):
        """
        Lists built images.

        Example response:

            [
                {
                    "Containers": -1,
                    "Created": 1667647604,
                    "Id": "sha256:7abb4084a569695100fd201d4db9a7a18eb32debb68b8ea291648550facd044a",
                    "Labels": {
                        "repo2docker.ref": "main",
                        "repo2docker.repo": "https://github.com/binderhub-ci-repos/cached-minimal-dockerfile",
                        "repo2docker.version": "2022.10.0+47.gb6098c0",
                    },
                    "ParentId": "sha256:70ce598462404da555bca9b60badb9c15d672c2661c690c30135eb2df7150d04",
                    "RepoDigests": None,
                    "RepoTags": ["binderhub-ci-repos/cached-minimal-dockerfile:main"],
                    "SharedSize": -1,
                    "Size": 294387098,
                    "VirtualSize": 294387098,
                },
            ]
        """
        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Image/operation/ImageList
        async with Docker() as docker:
            filters = json.dumps({"label": ["repo2docker-service.ref"]})
            built_images = await docker.images.list(filters=filters)
            return built_images
