import argparse
from argparse import Namespace


def arguementHandling() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="IP To Email", usage="To send a computer's IP address to an email account."
    )

    parser.add_argument(
        "-s",
        "--sender",
        nargs=1,
        type=str,
        required=True,
        help="The sender email address",
    )

    parser.add_argument(
        "-p",
        "--password",
        nargs=1,
        type=str,
        required=True,
        help="The sender email adress's password",
    )

    parser.add_argument(
        "-r",
        "--reciever",
        nargs=1,
        type=str,
        required=True,
        help="The recieving email address",
    )

    parser.add_argument(
        "-m",
        "--message",
        nargs=1,
        type=str,
        required=False,
        help="Message to append before the email address",
        default="Your computer's IP address is: ",
    )

    parser.add_argument(
        "-S",
        "--subject",
        nargs=1,
        type=str,
        required=False,
        help="The email's subject line",
        default="IP Address",
    )

    return parser.parse_args()
