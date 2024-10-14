"""
Open questions:
- How can a user provide a configuration file as part of using the FastAPI
  application as started via uvicorn?
- We now rely on a standalone class Repo2DockerService of base typ Configurable,
  loaded as part of starting the FastAPI application. Is that a good decision,
  or should we use Application as a base class instead somehow?
- Should we let this code start uvicorn, or should uvicorn start this?
"""

from traitlets.config.configurable import Configurable

from ..library.builder import Builder, MockedBuilder
from ..vendor import EntryPointType


class Repo2DockerService(Configurable):
    builder_class = EntryPointType(
        default_value=MockedBuilder,
        klass=Builder,
        entry_point_group="repo2docker_service.builders",
    ).tag(config=True)


config = Repo2DockerService()
