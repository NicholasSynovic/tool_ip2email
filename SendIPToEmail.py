import smtplib
import ssl
import subprocess
from getpass import getpass


class Email:

    # Some of the code below came from: https://realpython.com/
    # python-send-email

    def __init__(self, senderEmail: str, senderEmailPassword: str, recieverEmail: str):
        self.senderEmail = senderEmail
        self.senderEmailPassword = senderEmailPassword
        self.recieverEmail = recieverEmail

    def send(self, message: str) -> tuple:
        sender = self.getSenderAccount()
        port = 465
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            host="smtp.gmail.com", port=port, context=context
        ) as gmail:
            try:
                gmail.login(user=sender[0], password=sender[1])
            except smtplib.SMTPAuthenticationError:
                print(
                    """
You need to turn on "Less secure app access" in your Google account before\n
you can use this program (https://myaccount.google.com/lesssecureapps).\n
If this is not the issue then your EMAIL or PASSWORD is probably incorrect.
                    """
                )
                exit(1)
            gmail.sendmail(sender[0], self.getRecieverEmail(), message)
            gmail.close()

    def getSenderAccount(self) -> list:
        return [self.getSenderEmail(), self.getSenderEmailPassword()]

    def getSenderEmail(self) -> str:
        return self.senderEmail

    def getSenderEmailPassword(self) -> str:
        return self.senderEmailPassword

    def getRecieverEmail(self) -> str:
        return self.recieverEmail


def getIPs() -> tuple:
    output = subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE)
    return output.stdout.decode("utf-8").strip().split(" ")


def program() -> None:

    # Comment this code out and uncomment the below code in order to run this
    # application in production environments.

    senderEmail = input("What is your GMail email address? ")
    senderPassword = getpass("What is your GMail email password? ")
    reciverEmail = input("What is the recieving email address? ")

    # senderEmail = None
    # senderPassword = None
    # reciverEmail = None

    ipAddress = getIPs()[0]

    email = Email(
        senderEmail=senderEmail,
        senderEmailPassword=senderPassword,
        recieverEmail=reciverEmail,
    )

    message = (
        """
Subject: Network Pi IP Address

My IP Address is %s
"""
        % ipAddress
    )

    email.send(message=message)


program()
