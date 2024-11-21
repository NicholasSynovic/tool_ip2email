# 3. Use git tags to dynamically version the project

## Context

We have to be able to version the application somehow. We can either store the
version in an \_version.txt file, in `__init__.py` as `__version__`, in the
`pyproject.toml` file, or as a git tag. Each has their own uses, but we want to
be able to run `./ip2email --version` and get the version that we are currently
on. Thus maintaining more than one of these methods as overhead to the project
that is not necessary.

## Decision

We will use the `mtkennerly/poetry-dynamic-versioning` `poetry` plugin to
dynamically manage the version of `ip2email` via `git tag`s. In other words,
`git tag`s will set the version of the application, and this plugin will update
the package version for us automatically.

## Consequences

We will need to add a `-v, --version` flag to the `main.py` file to print out
the current version.
