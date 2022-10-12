"""
The DindBuilder relies on a local Docker daemon. It starts a container with
repo2docker in it and has mounted access to the same Docker daemon. The started
container then runs repo2docker to build an image.
"""
import json

from aiodocker import Docker

from .base import Build, Builder

BUILD_ENTRYPOINT = """
import argparse
import sys

from repo2docker import Repo2Docker

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--config",
    "-f",
    dest="config_files",
    action="append",
    default=[],
)
args, traitlet_args = argparser.parse_known_args(sys.argv[1:])

r2d = Repo2Docker()
for config_file in args.config_files:
    r2d.load_config_file(config_file)
r2d.parse_command_line(traitlet_args)
r2d.initialize()
r2d.start()
"""


class DindBuilder(Builder):
    @classmethod
    async def list_builds(cls):
        """
        Lists active builds.
        """
        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerList
        async with Docker() as docker:
            filters = json.dumps({"label": ["repo2docker-service.image-name"]})
            build_containers = await docker.containers.list(filters=filters)

        builds = [
            {
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
        """
        build_container_cmd = [
            "sh",
            "-c",
            " ".join(
                [
                    # Build entrypoint script and user provided repo2docker
                    # config is injected
                    'echo "$REPO2DOCKER_SERVICE_BUILD_ENTRYPOINT" > /tmp/build_entrypoint.py &&',
                    'echo "$REPO2DOCKER_SERVICE_REPO2DOCKER_CONFIG" > /tmp/repo2docker_config.json &&',
                    # Entrypoint is run
                    "exec python3 /tmp/build_entrypoint.py",
                    # ... with user managed config
                    "--config=/tmp/repo2docker_config.json",
                    f"--Repo2Docker.output_image_spec={build.image_name}",
                    f"--Repo2Docker.ref={build.ref}",
                    f"--Repo2Docker.repo={build.repo}",
                    # ... and builder managed config
                    "--Repo2Docker.run=False",
                    "--Repo2Docker.push=False",
                    "--Repo2Docker.user_id=65534",
                    "--Repo2Docker.user_name=nobody",
                ]
            ),
        ]

        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerCreate
        create_container_request_body = {
            "Cmd": build_container_cmd,
            "Image": "quay.io/jupyterhub/repo2docker:main",
            "Labels": {
                "repo2docker-service.image-name": build.image_name,
                "repo2docker-service.config": build.config,
            },
            "Env": [
                f"REPO2DOCKER_SERVICE_BUILD_ENTRYPOINT={BUILD_ENTRYPOINT}",
                f"REPO2DOCKER_SERVICE_REPO2DOCKER_CONFIG={build.config}",
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
            build_container = await docker.containers.run(
                config=create_container_request_body
            )
            # For debugging purposes, we could do...
            # async for line in build_container.log(stdout=True, stderr=True, follow=True):
            #     print(line)
            return build_container.id

    @classmethod
    async def stop_build(cls, id):
        """
        Stops a build.
        """
        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerKill
        async with Docker() as docker:
            build_container = docker.containers.container(id)
            await build_container.stop()

    @classmethod
    async def generate_build_logs(cls, id):
        """
        Yields log lines from running jupyter-repo2docker.

        Yeilds:
            Yields log lines.
        """
        # ref: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerLogs
        async with Docker() as docker:
            build_container = docker.containers.container(id)
            async for line in build_container.log(
                stdout=True, stderr=True, follow=True
            ):
                yield line
