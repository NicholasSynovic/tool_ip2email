import unittest
from email.message import EmailMessage

import emailComposer as ec


class Test_Email_Composer(unittest.TestCase):
    def test_emailBuilder(self):
        reciever: str = "tested@test.com"
        sender: str = "testing@test.com"
        subject: str = "Hello World"
        body: str = "Testing..."

        email = EmailMessage()
        email["To"] = reciever
        email["From"] = sender
        email["Subject"] = subject
        email.set_content(body)

        test: EmailMessage = ec.emailBuilder(reciever, sender, subject, body)

        self.assertTrue(test.get("To") == email.get("To"))
        self.assertTrue(test.get("From") == email.get("From"))
        self.assertTrue(test.get("Subject") == email.get("Subject"))
        self.assertTrue(test.get_content() == email.get_content())
