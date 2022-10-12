# How to make a release

`repo2docker-service` is a package available on [PyPI][] and [conda-forge][].
These are instructions on how to make a release.

## Pre-requisites

- Push rights to [github.com/consideratio/repo2docker-service][]
- Push rights to [conda-forge/repo2docker-service-feedstock][]

## Steps to make a release

1. Create a PR updating `docs/source/changelog.md` with [github-activity][] and
   continue only when its merged.

1. Checkout main and make sure it is up to date.

   ```shell
   git checkout main
   git fetch origin main
   git reset --hard origin/main
   ```

1. Update the version, make commits, and push a git tag with `tbump`.

   ```shell
   pip install tbump
   tbump --dry-run ${VERSION}

   # run
   tbump ${VERSION}
   ```

   Following this, the [CI system][] will build and publish a release.

1. Reset the version back to dev, e.g. `2.0.1.dev` after releasing `2.0.0`.

   ```shell
   tbump --no-tag ${NEXT_VERSION}.dev
   ```

1. Following the release to PyPI, an automated PR should arrive to
   [conda-forge/repo2docker-service-feedstock][] with instructions.

[github-activity]: https://github.com/executablebooks/github-activity
[github.com/consideratio/repo2docker-service]: https://github.com/consideratio/repo2docker-service
[pypi]: https://pypi.org/project/repo2docker-service/
[conda-forge]: https://anaconda.org/conda-forge/repo2docker_service
[conda-forge/repo2docker-service-feedstock]: https://github.com/conda-forge/repo2docker-service-feedstock
[ci system]: https://github.com/consideratio/repo2docker-service/actions/workflows/release.yaml
