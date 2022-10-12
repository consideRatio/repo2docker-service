from .base import Registry
from .docker import DockerRegistry
from .docker_daemon import DockerDaemonRegistry
from .mocked import MockedRegistry

__all__ = [
    Registry,
    DockerRegistry,
    DockerDaemonRegistry,
    MockedRegistry,
]
