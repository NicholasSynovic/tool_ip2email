# 2. Use PyInstaller to create a single file application

## Context

There is currently no way to distribute this application aside from building it
from source. While the app is small enough to be built from source, it is also
small enough to be a single binary. Python does not include a utlity to do this
anymore (i.e. `freeze`), so an alternative will have to be created.

## Decision

We will use `PyInstaller` to bundle the code into a single binary that can be
distributed outside of the project. This binary will be able to run without a
`python3.10` interpreter or `venv`. Additionally, the `make build` directive
will be updated to support bundling the project with `PyInstaller`.

## Consequences

As `PyInstaller` does not support cross-platform building, a GitHub CI action
will need to be created to support MacOS, Windows, and Linux. This action will
run once per `git tag`.
