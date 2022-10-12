"""
The DindBuilder relies on a local Docker daemon. It starts a container that in
turn is provided access to the same Docker daemon via mounted volumes. The
started container then runs repo2docker to build an image.

A computer with a Docker daemon ->
    A build container using the same Docker daemon ->
        Runs repo2docker to build an image
"""
import json

from aiodocker import Docker

from .base import BaseBuilder, Build


class DindBuilder(BaseBuilder):
    @classmethod
    async def list_builds(cls):
        """
        Lists active builds.

        Returns:
            builds (list):
                A list of dictionaries with the keys "image_name", "repo",
                "ref", "config".
        """
        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerList
        async with Docker() as docker:
            filters = json.dumps({"label": ["repo2docker-service.image-name"]})
            build_containers = await docker.containers.list(filters=filters)

        builds = [
            {
                "repo": bc["Labels"]["repo2docker-service.repo"],
                "ref": bc["Labels"]["repo2docker-service.ref"],
                "image_name": bc["Labels"]["repo2docker-service.image-name"],
                "config": bc["Labels"]["repo2docker-service.config"],
            }
            for bc in build_containers
        ]
        return builds

    @classmethod
    async def start_build(cls, build: Build):
        """
        Starts a build.

        Start a build by starting a container with the local Docker daemon,
        which is also mounted for use within the container, and run repo2docker
        that can make use of it to do the build.

        Args:
            build:
                Representing "image_name", "repo", "ref", and "config".
        """
        build_container_cmd = [
            "sh",
            "-c",
            " ".join(
                [
                    "echo $REPO2DOCKER_SERVICE_CONFIG > /tmp/repo2docker_config.json",
                    "&&",
                    "jupyter-repo2docker",
                    "--no-run",
                    "--push",
                    "--user-id=1000",
                    "--user-name=jovyan",
                    "--debug",
                    "--config=/tmp/repo2docker_config.json",
                    f"--ref={build.ref}",
                    f"--image-name={build.image_name}",
                    f"{build.repo}",
                ]
            ),
        ]

        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerCreate
        create_container_request_body = {
            "Cmd": build_container_cmd,
            "Image": "quay.io/jupyterhub/repo2docker:main",
            "Labels": {
                "repo2docker-service.repo": build.repo,
                "repo2docker-service.ref": build.ref,
                "repo2docker-service.image-name": build.image_name,
                "repo2docker-service.config": build.config,
            },
            "Env": [
                f"REPO2DOCKER_SERVICE_CONFIG={build.config}",
            ],
            "HostConfig": {
                "Binds": [
                    "/var/run/docker.sock:/var/run/docker.sock",
                ],
            },
            "Volumes": {
                "/var/run/docker.sock": {
                    "bind": "/var/run/docker.sock",
                    "mode": "rw",
                },
            },
            "StopSignal": "SIGKILL",
            "StopTimeout": 0,
        }
        async with Docker() as docker:
            await docker.containers.run(config=create_container_request_body)

    @classmethod
    async def stop_build(cls, image_name):
        """
        Stops a build.

        Args:
            image_name: identifies the build
        """
        async with Docker() as docker:
            bc = await cls._get_build_container(docker, image_name)

            # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerKill
            await bc.stop()

    @classmethod
    async def generate_build_logs(cls, image_name):
        """
        Yields log lines from running jupyter-repo2docker.

        Args:
            image_name: identifies the build

        Yeilds:
            Yields log lines.
        """
        async with Docker() as docker:
            bc = await cls._get_build_container(docker, image_name)

            # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerLogs
            async for line in bc.log(stdout=True, stderr=True, follow=True):
                yield line

    @classmethod
    async def _get_build_container(cls, docker, image_name):
        filters = json.dumps(
            {"label": [f"repo2docker-service.image-name={image_name}"]}
        )
        build_containers = await docker.containers.list(filters=filters)

        if build_containers:
            return build_containers[0]
        else:
            return None
