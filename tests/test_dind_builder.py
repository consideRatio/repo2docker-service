import pytest

from repo2docker_service.library.builder import Build, DindBuilder


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
async def test_start_list_log_stop_build(build):
    # test start
    build_id = await DindBuilder.start_build(build)

    # test list
    builds = await DindBuilder.list_builds()
    assert isinstance(builds, list)

    # test log
    log_line_yielded = False
    async for _ in DindBuilder.generate_build_logs(build_id):
        log_line_yielded = True
        break
    assert log_line_yielded, "not a single line of logs detected"

    # test stop
    await DindBuilder.stop_build(build_id)
