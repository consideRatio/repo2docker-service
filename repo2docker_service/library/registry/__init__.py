from .base import BaseRegistry
from .docker import DockerRegistry
from .docker_daemon import DockerDaemonRegistry
from .mocked import MockedRegistry

__all__ = [
    BaseRegistry,
    DockerRegistry,
    DockerDaemonRegistry,
    MockedRegistry,
]
