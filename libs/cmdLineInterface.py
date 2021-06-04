import subprocess


def commandLineInterface(command: list) -> str:
    rawByteStream: subprocess.CompletedProcess[str] = subprocess.run(
        command, stdout=subprocess.PIPE
    )
    decodedByteStream: str = rawByteStream.stdout.decode("utf-8").strip()

    return decodedByteStream
