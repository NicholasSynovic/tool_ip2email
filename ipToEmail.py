from libs import cmdLineInterface
from libs import cmdLineParser
from libs import emailComposer
from libs import logger

if __name__ == "__main__":
    log = logger.createFile()
    logger.logToFile(message="Create log file " + log, filename=log)

    args = cmdLineParser.arguementHandling()
    logger.logToFile(message="Get command line arguements", filename=log)

    senderEmailAddress = args.sender[0]
    senderEmailPassword = args.password[0]
    recieverEmailAddress = args.reciever[0]
    subjectLine = args.subject
    message = args.message

    logger.logToFile(
        message="Assign command line arguements to variables", filename=log
    )
    logger.logToFile(
        message="Sender Email Address: " + senderEmailAddress, filename=log
    )
    logger.logToFile(
        message="Sender Email Password: " + senderEmailPassword, filename=log
    )
    logger.logToFile(
        message="Reciever Email Address: " + recieverEmailAddress, filename=log
    )
    logger.logToFile(message="Subject: " + subjectLine, filename=log)
    logger.logToFile(message="Message: " + message, filename=log)

    ipAddress = cmdLineInterface.commandLineInterface(["hostname", "-I"])
    logger.logToFile(message="IP address is " + ipAddress, filename=log)
    logger.logToFile(message="Message: " + message, filename=log)

    message = message + ipAddress
    logger.logToFile(message='Create email message: "' + message + '"', filename=log)

    email = emailComposer.emailBuilder(
        reciever=recieverEmailAddress,
        sender=senderEmailAddress,
        subject=subjectLine,
        body=message,
    )
    logger.logToFile(message="Create email object", filename=log)

    sendWithEmailPassword = emailComposer.sendEmail(
        reciever=recieverEmailAddress,
        sender=senderEmailAddress,
        password=senderEmailPassword,
        subject=subjectLine,
        email=email,
    )

    if sendWithEmailPassword:
        logger.logToFile(message="Email sent to " + recieverEmailAddress, filename=log)
        exit(0)
    else:
        logger.logToFile(message="Email not sent", filename=log)

        logger.logToFile(
            message="You need to provide an app password to use this application.\n        If this is not the issue then your email or password is incorrect.",
            filename=log,
        )
        exit(1)
