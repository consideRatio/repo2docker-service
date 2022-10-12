# repo2docker-service

[![Documentation build status](https://img.shields.io/readthedocs/repo2docker-service?logo=read-the-docs)](https://repo2docker-service.readthedocs.io/en/latest/?badge=latest)
[![GitHub Workflow Status - Test](https://img.shields.io/github/workflow/status/consideratio/repo2docker-service/Test?logo=github&label=tests)](https://github.com/consideratio/repo2docker-service/actions)

`repo2docker-service` is a [FastAPI][] based web application to be run as a
[JupyterHub][] [Service][]. It can enable JupyterHub users to run
[repo2docker][] directly via a primitive user interface exposed at
https://your-hub.example.com/services/repo2docker, as well as a more advanced
functionality to be built with its provided REST API.

[jupyterhub]: https://github.com/jupyterhub/jupyterhub#readme
[service]: https://jupyterhub.readthedocs.io/en/stable/reference/services.html
[repo2docker]: https://github.com/jupyterhub/repo2docker#readme
[fastapi]: https://fastapi.tiangolo.com/

## Install

```shell
pip install repo2docker-service
```

## Run

```shell
uvicorn repo2docker_service:app
```
