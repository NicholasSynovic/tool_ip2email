import smtplib
import ssl
from email.message import EmailMessage


def createEmail(
    recipient: str,
    email: str,
    subject: str,
    body: str,
) -> EmailMessage:
    email: EmailMessage = EmailMessage()
    email["To"] = recipient
    email["From"] = email
    email["Subject"] = subject
    email.set_content(body)

    return email


def sendEmail(
    sender: str,
    password: str,
    email: EmailMessage,
) -> bool:
    gmailSMTPPort = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        host="smtp.gmail.com",
        port=gmailSMTPPort,
        context=context,
    ) as gmailConnection:
        try:
            gmailConnection.login(user=sender, password=password)
        except smtplib.SMTPAuthenticationError:
            return False

        gmailConnection.sendmail(
            from_addr=sender,
            to_addrs=email["To"],
            msg=email.as_string(),
        )
        gmailConnection.close()

    return True
