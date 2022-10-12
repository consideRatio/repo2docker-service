# Structure of the Python package

| Code        | Note                                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| `app/`      | A FastAPI web application, to be run with uvicorn.                                                                       |
| `frontend/` | Source code for static assets to be served by the FastAPI web application, providing a basic UI to consume the REST API. |
| `library/`  | Builder and Registry classes classes that the FastAPI web application use to do actual work.                             |
| `vendor/`   | Snippets of source code vendored from other projects.                                                                    |
