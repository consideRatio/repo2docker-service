# Structure of the Python package

| Code        | Note                                                                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app/`      | Defines a FastAPI web application.                                                                                                                                  |
| `library/`  | Defines builder and registry classes classes that the FastAPI app can be configured to use to perform actual work.                                                  |
| `frontend/` | Defines source code to build static assets to be served by the FastAPI app.                                                                                         |
| `static/`   | Includes pre-defined and dynamically built static assets (html, css, js) to be served by the FastAPI app, providing a basic user interface to consume the REST API. |

## Contributing

- Use of [Google docstrings][]

[google docstrings]: https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings
