from datetime import datetime
from email.message import EmailMessage

import click

from ip2email import emailHandler, getVersion, ip


@click.command()
@click.option(
    "-e",
    "--email-address",
    "emailAddress",
    type=str,
    nargs=1,
    required=True,
    help="Email address to send the email from",
)
@click.option(
    "-p",
    "--password",
    "password",
    type=str,
    nargs=1,
    required=True,
    help="Google app password of the sender's email address",
)
@click.option(
    "-r",
    "--recipient",
    "recipient",
    type=str,
    nargs=1,
    required=True,
    help="Recipient of the email address",
)
@click.version_option(version=getVersion())
def main(emailAddress: str, password: str, recipient: str) -> None:
    """
    Send an email containing the device's host name and IP address to specific recipient.

    The host name is located in the subject of the email address. The format of the subject is:

    {hostname}'s IP Address (DAY NAME, MONTH DAY DATE)


    The IP address is the sole information in the body.
    """  # noqa: E501
    ipAddress: str = ip.getIPAddress()
    hostname: str = ip.getHostname()

    subject: str = f"{hostname}'s IP Address ({datetime.now().strftime('%A, %B %d')})"  # noqa: E501

    email: EmailMessage = emailHandler.createEmail(
        recipient=recipient,
        subject=subject,
        body=ipAddress,
    )

    sentEmail: bool = emailHandler.sendEmail(
        sender=emailAddress,
        password=password,
        email=email,
    )

    if sentEmail is True:
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
