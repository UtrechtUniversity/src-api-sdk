This project contains an SDK for interacting with the API of SURF ResearchCloud, a custom cloud provider. swagger definitions for the api are in the `swagger` directory.

Goals:

- simple sdk
- user-friendly
- human-understandable

Dependencies in pyproject.toml. Check whether a VIRTUAL_ENV is active, otherwise use .venv if it exists.

Prefer using standard libraries (not third-party dependencies) over writing own code. 

Tests must not hit live endpoints; use mocks instead.

- Lint with `ruff check src tests`.
- `mypy` for type checking.
- `pytest` for tests.
