# `ip2email` (IP To Email)

> A small utility to email a device's local IP address

## Table of Contents

- [`ip2email` (IP To Email)](#ip2email-ip-to-email)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How To Install](#how-to-install)
  - [How To Run](#how-to-run)

## About

This is a small utility to send an IP address of a UNIX device via GMail to an
email address.

The format of the email address is:

`{hostname}'s IP Address (DAY NAME, MONTH DAY DATE)`

## How To Install

Assuming you have `git clone`d the repository:

1. `make create-dev`
1. `source env/bin/activate`
1. `make build`

## How To Run

- `ip2email --help`

```shell
Usage: ip2email [OPTIONS]

Options:
  -e, --email-address TEXT  Email address to send the email from  [required]
  -p, --password TEXT       Google app password of the sender's email address
                            [required]
  -r, --recipient TEXT      Recipient of the email address  [required]
  --version                 Show the version and exit.
  --help                    Show this message and exit.
```

You can set and get a Google app password
[here](https://myaccount.google.com/apppasswords).
