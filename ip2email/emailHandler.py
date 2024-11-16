import smtplib
import ssl
from email.message import EmailMessage


def createEmail(
    recipient: str,
    subject: str,
    body: str,
) -> EmailMessage:
    """
    Method to create a simple EmailMessage object

    :param recipient: The email address to recieve the message
    :type recipient: str
    :param subject: The subject of the email message
    :type subject: str
    :param body: The body of the email message
    :type body: str
    :return: A simple Python EmailMessage object
    :rtype: EmailMessage
    """
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
    """
    Send an EmailMessage object via GMail to an email address

    :param sender: The GMail account to send the email from
    :type sender: str
    :param password: The Google App Password of the GMail account
    :type password: str
    :param email: The EmailMessage object
    :type email: EmailMessage
    :return: Return True if the message is sent, else return False
    :rtype: bool
    """
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
