import time


def createFile() -> None:
    filename = "iptoemail_{}.txt".format(time.time())
    with open(file=filename, mode="w") as temp:
        temp.close()


def logToFile(message: str, filename: str) -> bool:
    message = "[{}]    {}".format(time.time(), message)

    with open(file=filename, mode="a") as logfile:
        logfile.write(message)
        logfile.close()
