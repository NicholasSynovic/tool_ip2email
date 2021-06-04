import email
from email.message import EmailMessage


def emailBuilder(reciever: str, sender: str, subject: str, body: str) -> EmailMessage:
    email = EmailMessage()
    email["To"] = reciever
    email["From"] = sender
    email["Subject"] = subject
    email.set_content(body)

    return email
