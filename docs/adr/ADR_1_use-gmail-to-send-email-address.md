# 1. Use GMail to send email address

## Context

The client device needs to send the email out to a recipient. Rather than
rolling our own email service, we can leverage GMail's SMTP service to send
messages.

## Decision

This application will initially be limited to sending emails via GMail. It will
require that the sender's email address is a GMail account.

## Consequences

We are limited to 50 messages a day. Additionally, the user will need to setup
an app password with Google and pass this into the application.
