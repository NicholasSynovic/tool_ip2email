import unittest

import cmdLineInterface as cli


class Test_IP_Address(unittest.TestCase):
    def test_commandLineInterface(self):
        command: list = ["echo", "hello world"]

        self.assertTrue(cli.commandLineInterface(command) == "hello world")
