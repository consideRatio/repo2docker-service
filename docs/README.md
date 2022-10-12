# About the documentation

This documentation is automatically built on each commit [as configured on
ReadTheDocs](https://readthedocs.org/projects/repo2docker-service/) and in the
`.readthedocs.yaml` file, and made available on
[repo2docker-service.readthedocs.io](https://repo2docker-service.readthedocs.io/en/latest/).

The documentation is meant to be structured according to the Diataxis framework
as documented in https://diataxis.fr/.

## Local documentation development

```shell
cd docs
pip install -r requirements.txt
```

```shell
# automatic build and livereload enabled web-server
make devenv

# automatic check of links validity
make linkcheck
```
