# Implementation

## Technical stack

- [FastAPI][] web application
  - Featuring [traitlets][] based configuration
  - Featuring a Python library as a backend for the REST API
    - Interacts with a local Docker daemon
      - Using the [aiodocker][] Python client
      - Builds new images using repo2docker from within a container started
        using an official repo2docker image.
    - Interacts with a remote container registry
      - Using the [Docker Registry v2 API][], via [mybinder.org's container
        registry client][]
      - Uploads, lists, and deletes images
  - Featuring a REST API
  - Featuring a primitive frontend application to use the REST API
    - Using [React][] for building user interfaces
    - Using [chakra-ui][] for React user interface components
    - Using [webpack][] to compile frontend source code into the static assets
    - Using [Babel][] to compile javascript for browser compatibility
  - Featuring authentication and authorization
    - Using [JupyterHub][] as a OAuth2 provider
    - Using [JupyterHub RBAC][]'s system with pre-configured roles and scopes
      assigned to users and groups of users.
- Documentation with [ReadTheDocs][], using [Sphinx][], [sphinx-book-theme][],
  and [myst-parser][]
  - How to deploy with a [Uvicorn][] web server
- CI with [GitHub Actions][] running [PyTest][]

[fastapi]: https://fastapi.tiangolo.com/
[traitlets]: https://traitlets.readthedocs.io/en/stable/
[aiodocker]: https://aiodocker.readthedocs.io/en/stable/
[docker registry v2 api]: https://docs.docker.com/registry/spec/api/
[mybinder.org's container registry client]: https://github.com/jupyterhub/binderhub/blob/master/binderhub/registry.py
[react]: https://reactjs.org/
[chakra-ui]: https://github.com/chakra-ui/chakra-ui
[webpack]: https://webpack.js.org/
[babel]: https://babeljs.io/
[jupyterhub]: https://jupyterhub.readthedocs.io/en/stable/
[jupyterhub rbac]: https://jupyterhub.readthedocs.io/en/stable/rbac/index.html
[readthedocs]: https://readthedocs.org/
[sphinx]: https://www.sphinx-doc.org/en/master/
[sphinx-book-theme]: https://sphinx-book-theme.readthedocs.io/en/stable/
[myst-parser]: https://myst-parser.readthedocs.io/en/stable/
[uvicorn]: https://www.uvicorn.org/
[github actions]: https://github.com/features/actions
[pytest]: https://docs.pytest.org/en/stable/
