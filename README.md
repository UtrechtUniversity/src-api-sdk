# A simple Python SDK and CLI for SURF ResearchCloud.

- Install as a package in your venv from GitHub with `pip install git+`, or locally with `pip install -e .`
- To use the SDK from inside your Python code: `from researchcloud.client import ResearchCloudClient`, ...
- To use the packaged CLI tool: see below.

*Todo*: link to API docs.

### Special case: current workspace

This package includes a convenience module to perform operations on the *current workspace*. That is, if your code is run on a ResearchCloud workspace, the module will allow you to conveniently e.g. pause that workspace.

```python
import researchcloud.current_workspace as current_workspace

# current_workspace takes care of client setup and looking up the current workspace's SRC ID.
current_workspace.pause() # will attempt to lookup RESEARCH_CLOUD_TOKEN from env. You can optionally pass in token=....
```

## CLI

In a venv with this pacakge installed, use the `researchcloud` command to interact with the ResearchCloud API. For example:

`researchcloud get-application-offerings --dry-run --by-owner --co "My CO"`

See `researchcloud --help` for other commands.

### Note on application types

For the SRC API, workspaces, catalog items, networks, etc. are all "application offerings". When using `get-application-offerings`, omitting `--type` means that all application
types are included. Use `--type` when you want to restrict the results to one application type (e.g. `workspace`, `network`, ...).

## Contributing

- Run the linter with `.venv/bin/ruff check .`.
- Type checking with `mypy`
- Run tests with `pytest`

`AGENTS.md` expects swagger definitions for the SRC API services in the `swagger` directory. These are currently not committed to the repo.
