from ip2email import ip


# @click.command()
# @click.option(
#     "-e",
#     "--email",
#     "email",
#     type=str,
#     nargs=1,
#     required=True,
#     help="Email address to send the email from",
# )
def main() -> None:
    ipAddress: str = ip.getIPAddress()
    hostname: str = ip.getHostname()

    print(ipAddress, hostname)


if __name__ == "__main__":
    main()
