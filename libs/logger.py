import time
from datetime import datetime


def createFile() -> str:
    filename = "iptoemail_{}.txt".format(time.time())

    with open(file=filename, mode="w") as temp:
        temp.close()

    return filename


def logToFile(message: str, filename: str) -> None:
    currentTime = datetime.now().strftime("%H:%M:%S")
    message = "[{}]    {}".format(currentTime, message)

    with open(file=filename, mode="a") as logfile:
        logfile.write(message)
        logfile.close()
