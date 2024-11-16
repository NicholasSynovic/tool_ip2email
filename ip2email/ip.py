import subprocess  # nosec


def getIPAddress() -> str:
    """
    Get the local IP address of the device via ifconfig.

    The full shell command is:

    ifconfig -a | grep inet | head -n 1 | sed 's/.* //'

    :return: The local IP address
    :rtype: str
    """
    return subprocess.run(
        args="ifconfig -a | grep inet | head -n 1 | sed 's/.* //'",
        capture_output=True,
        shell=True,
        text=True,
    ).stdout.strip()  # nosec


def getHostname() -> str:
    """
    Get the host name of the device via hostname.

    The full shell command is:

    hostname

    :return: The host name of the device
    :rtype: str
    """
    return subprocess.run(
        args="hostname",
        capture_output=True,
        shell=True,
        text=True,
    ).stdout.strip()  # nosec
