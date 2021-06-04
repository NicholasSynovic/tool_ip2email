import email
from email import message
import smtplib
import ssl
from email.message import EmailMessage
import logger


def emailBuilder(reciever: str, sender: str, subject: str, body: str) -> EmailMessage:
    email = EmailMessage()
    email["To"] = reciever
    email["From"] = sender
    email["Subject"] = subject
    email.set_content(body)

    return email


def sendEmail(
    reciever: str, sender: str, password: str, subject: str, email: EmailMessage
) -> bool or list:
    gmailSMTPPort = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        host="smtp.gmail.com", port=gmailSMTPPort, context=context
    ) as gmailConnection:
        try:
            gmailConnection.login(user=sender, password=password)
        except smtplib.SMTPAuthenticationError as authenticationError:
            return [
                authenticationError.str(),
                'You need to turn on "Less secure app access" in your Google account beforeyou can use this program (https://myaccount.google.com/lesssecureapps).',
                "If this is not the issue then your EMAIL or PASSWORD is probably incorrect.",
            ]

        gmailConnection.sendmail(
            from_addr=sender, to_addrs=reciever, msg=email.as_string()
        )
        gmailConnection.close()

    return True
