import pytest

from . import Build, DindBuilder


async def test_list_builds():
    builds = await DindBuilder.list_builds()
    print(builds)
    assert isinstance(builds, list)


@pytest.mark.parametrize(
    "build",
    [
        Build(
            image_name="binderhub-ci-repos/cached-minimal-dockerfile:main",
            repo="https://github.com/binderhub-ci-repos/cached-minimal-dockerfile",
            ref="main",
            config="{}",
        ),
    ],
)
async def test_start_build(build):
    await DindBuilder.start_build(build)


@pytest.mark.parametrize(
    "image_name",
    [
        "binderhub-ci-repos/cached-minimal-dockerfile:main",
    ],
)
async def test_generate_build_logs(image_name):
    async for line in DindBuilder.generate_build_logs(image_name):
        assert line
        return
    assert False, "not a single line of logs detected"


@pytest.mark.parametrize(
    "image_name",
    [
        "binderhub-ci-repos/cached-minimal-dockerfile:main",
    ],
)
async def test_stop_build(image_name):
    await DindBuilder.stop_build(image_name)
