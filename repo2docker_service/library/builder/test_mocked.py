import pytest

from . import Build, MockedBuilder


async def test_list_builds():
    builds = await MockedBuilder.list_builds()
    print(builds)
    assert isinstance(builds, list)


@pytest.mark.parametrize(
    "build",
    [
        Build(
            image_name="binderhub-ci-repos/cached-minimal-dockerfile:test",
            repo="https://github.com/binderhub-ci-repos/cached-minimal-dockerfile",
            ref="test",
            config="{}",
        ),
    ],
)
async def test_start_build(build):
    await MockedBuilder.start_build(build)


@pytest.mark.parametrize(
    "image_name",
    [
        "binderhub-ci-repos/cached-minimal-dockerfile:test",
    ],
)
async def test_generate_build_logs(image_name):
    async for line in MockedBuilder.generate_build_logs(image_name):
        assert line
        return
    assert False, "not a single line of logs detected"


@pytest.mark.parametrize(
    "image_name",
    [
        "binderhub-ci-repos/cached-minimal-dockerfile:test",
    ],
)
async def test_stop_build(image_name):
    await MockedBuilder.stop_build(image_name)
