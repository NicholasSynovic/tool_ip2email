# 0. Use shell commands to identify IP address

## Context

This tool needs to be able to identify the IP address of a UNIX system.

As we are running this on a UNIX system, we will have access to UNIX shell
processing via the `subprocess` module.

## Decision

We will use the following shell command to identify the IP address:

```shell
ifconfig -a | grep inet | head -n 1 | sed 's/.* //'
```

## Consequences

This command will be limited to systems that have all of the tooling installed.

Additionally, `subprocess` can be used to run malicous commands if not properly
handled.
