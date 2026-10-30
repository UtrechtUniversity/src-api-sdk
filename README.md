# A simple Python SDK and CLI for SURF ResearchCloud.

- Install as a package in your venv from GitHub with `pip install git+`, or locally with `pip install -e .`
- Import the package from [src/researchcloud/](/Users/3060845/Code/uu/src/api_explorations/src/researchcloud).

## CLI

In a venv with this pacakge installed, use the `researchcloud` command to interact with the ResearchCloud API. For example:

`researchcloud get-application-offerings --dry-run --by-owner --co "My CO"`

See `researchcloud --help` for other commands.

### Note on application types

For the SRC API, workspaces, catalog items, networks, etc. are all "application offerings". When using `get-application-offerings`, omitting `--type` means that all application
types are included. Use `--type` when you want to restrict the results to one application type (e.g. `workspace`, `network`, ...).

## Contributing

- Run the linter with `.venv/bin/ruff check .`.
- Run tests with `pytest`

