# A FastAPI web application

This [FastAPI][] based web application provides a REST API under `/api/v1`. The
REST API is wrapping a configured [Builder][] and [Registry][] class'
functions.

A UI to use the REST API is provided under `/`, which is maintained in the
[frontend][] folder.

## Development notes

To run the application, use [uvicorn][] like below from the root directory of
this git project.

```shell
pip install -e ".[dev,test]"

uvicorn repo2docker_service:app --reload
```

## References

[builder]: ../library/builder/
[fastapi's suggested structure]: https://fastapi.tiangolo.com/tutorial/bigger-applications/
[frontend]: ../frontend/
[registry]: ../library/registry/
[uvicorn]: https://www.uvicorn.org/
