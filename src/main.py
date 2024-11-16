import click


@click.command()
@click.option(
    "-e",
    "--email",
    "email",
    type=str,
    nargs=1,
    required=True,
    help="Email address to send the email from",
)
def main(email: str) -> None:
    pass


if __name__ == "__main__":
    main()
