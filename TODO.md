# Notes for myself

Scope:

- locked into repo2docker, jupyterhub, traitlets
- use general traitlets application config to avoid dedicated pass through of config

`docs/`

- DONE: bootstrap myst

`library/builder/`

- DONE: Add DindBuilder

`library/registry/`

- **NEXT**: Add DockerDaemonRegistry
- Add DockerRegistry

`frontend/`

- DONE: Initialize a frontend application
  - DONE: React
  - DONE: Webpack
  - DONE: Babel
  - DONE: Jest
  - DONE: Chakra-ui

`app/`

- **NEXT**: Define REST API relying on `MockedRegistry`
- DONE: Define REST API relying on `MockedBuilder`
- DONE: OpenAPI documentation
  - DONE: Bootstrap it
  - DONE: Add whats needed for it to reflect our REST API
- Add configuration system based on traitlets
  - Allow configuration of builder
- Add authentication against JupyterHub, look at:
  - https://github.com/kbatch-dev/kbatch/tree/main/kbatch-proxy
  - https://github.com/jupyterhub/jupyterhub/blob/main/examples/
- Add authorization against JupyterHub

Python packaging:

- Figure out what to include in the source manifest and how to declare that.
- Figure out what to include in the wheel and how to declare that.

# tljh-repo2docker overview

## Web API

GET environments

GET api/environments/:name/logs
DELETE api/environments
POST api/environments

## Python API

build_image
list_containers
list_images

# binderhub overview

The only Web API in BinderHub relevant to compare with is `/build`, which is a
very high level API only accepting `GET`. It streams JSON messages about build
and launch progress and when it concludes allows the user to redirect to the
launched server.

## Web API

### [MainHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/main.py#L27) - `/`

GET, index.html and bundle.js, calls /build and redirects to the started user server

### [ParameterizedMainHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/main.py#L44) - `/v2/([^/]+)/(.+)`

GET, loading.html and bundle.js, calls /build and redirects to the started user server. With this, users can launch directly without pressing a launch button.

### [LegacyRedirectHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/main.py#L129) - `/repo/([^/]+)/([^/]+)(/.*)?`

GET, redirects to /v2/..., so its in practice /v1/

### [BuildHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/builder.py#L143) - `/build/([^/]+)/(.+)`

GET, REST API, streams JSON messages about build and launch progress.

The handler manage the following logic

1. Validate "repo provider" (invalid? banned?)
2. Generate deterministic image name and build name
3. Check registry or local docker daemon for image name
4. If the image was found: launch server and return
5. Instanciate a BuildClass object based on `build_class` config, and start an image build followed by pushing it to the registry if needed, stream logs until completion
6. Launch server and return
7. (Following this, users could redirect to the server)

### [AboutHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/base.py#L220) - `/about`

GET, about.html, provides basic information

### [VersionHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/base.py#L236) - `/versions`

GET, REST API, emits JSON about versions for "builder" and "binderhub"

### [MetricsHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/metrics.py#L6) - `/metrics`

GET, emits metrics for Prometheus to scrape

### [HealthHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/health.py#L93) - `/health`

GET and HEAD, REST API, emits JSON about deployment health status under keys "ok" and "checks"

### [ConfigHandler](https://github.com/jupyterhub/binderhub/blob/3eb81bba1dbdd069c762bc31939a2619f4456cb5/binderhub/config.py#L4) - `/_config`

GET, REST API, emits JSON with repo providers configuration.

Used by index.js to update the DOM dynamically using JQuery. The DOM updated is the input fields and labels for "repository" and "ref" in index.html.

- PR introducing it, https://github.com/jupyterhub/binderhub/pull/1038
- index.js, https://github.com/jupyterhub/binderhub/blob/a8e3444a20d01b1937d3a92d59fb3651e46b5b58/binderhub/static/js/index.js#L64-L97
- index.html, #repository, https://github.com/jupyterhub/binderhub/blob/81017b414877aa8d2d46699804816b08af3b5bca/binderhub/templates/index.html#L49
- index.html, #ref, https://github.com/jupyterhub/binderhub/blob/81017b414877aa8d2d46699804816b08af3b5bca/binderhub/templates/index.html#L55
