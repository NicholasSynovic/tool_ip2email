import smtplib
import ssl
from email.message import EmailMessage


def emailBuilder(
    reciever: str,
    sender: str,
    subject: str,
    body: str,
) -> EmailMessage:
    email = EmailMessage()
    email["To"] = reciever
    email["From"] = sender
    email["Subject"] = subject
    email.set_content(body)

    return email


def sendEmail(
    reciever: str,
    sender: str,
    password: str,
    subject: str,
    email: EmailMessage,
) -> bool | list:
    gmailSMTPPort = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        host="smtp.gmail.com", port=gmailSMTPPort, context=context
    ) as gmailConnection:
        try:
            gmailConnection.login(user=sender, password=password)
        except smtplib.SMTPAuthenticationError:
            return False

        gmailConnection.sendmail(
            from_addr=sender, to_addrs=reciever, msg=email.as_string()
        )
        gmailConnection.close()

    return True
