import email
import smtplib
import ssl
from email.message import EmailMessage


def emailBuilder(reciever: str, sender: str, subject: str, body: str) -> EmailMessage:
    email = EmailMessage()
    email["To"] = reciever
    email["From"] = sender
    email["Subject"] = subject
    email.set_content(body)

    return email


def sendEmail(
    reciever: str, sender: str, password: str, subject: str, email: EmailMessage
) -> bool:
    gmailSMTPPort = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=gmailSMTPPort, context=context) as gmailConnection:
      try:
        gmailConnection.login(user=sender, password=password)
      except smtplib.SMTPAuthenticationError:
