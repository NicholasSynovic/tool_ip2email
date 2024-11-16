import subprocess  # nosec


def getIPAddress() -> str:
    return subprocess.run(
        args="ifconfig -a | grep inet | head -n 1 | sed 's/.* //'",
        capture_output=True,
        shell=True,
        text=True,
    ).stdout.strip()  # nosec
