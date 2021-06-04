# IP To Email

## About

This is a Python3 tool to send the email address of a computer to a designated email address.

### Note

This program does require that the computer already be connected to the internet. So make sure that this program is ran after a network connection is established if you are planning to use this script on boot.

## Use Case

Sending a computer's IP address to an email address on boot.

## Requirements

1. Have Python 3.9+ installed
2. Have a GMail account
3. Make sure that GMail account allows for unauthorized applications

## How to Use

0. Make sure that you have  on your computer.
1. Execute `python3 ipToEmail.py -s SENDER_EMAIL_ADDRESS -p SENDER_EMAIL_PASSWORD -r RECIEVER_EMAIL_ADDRESS`

### Note

- If you would like to save the credentials to a file, add the `--save` arguement at the end of the string
- If you would like to load data from a file, execute `python3 ipToEmail.py`
- You can execute `python3 ipToEmail.py -h` or `python3 ipToEmail.py --help` to see a full list of arguements and their descriptions

## How to Contribute

There are several ways that you can contribue:

1. Report issues [here](https://github.com/NicholasSynovic/GitHub-Repository-Displayer/issues)
2. Fork the code and improve it!
