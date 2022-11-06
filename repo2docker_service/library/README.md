# The library

The library's purpose is to provide functionality that the FastAPI web
application can be configured to rely on. The app will need a Builder and a
Registry.

## Builder

The chosen Builder should execute repo2docker in some way (in sub-process,
docker container, k8s pod, etc.), and accept repo2docker native configuration in
a JSON format as well as an arbitrary JSON state that can be retrieved later.

Besides starting repo2docker builds, a Builder should also be able to list
builds, stop a build, and get logs from a build.

## Registry

The chosen Registry should be a location where finished Builds arrive as image
artifacts. It could be a local docker daemon, a remote docker registry, or
similar.

A Registry should support listing and deleting built images.
