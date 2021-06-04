import unittest

import cmdLineInterface as cli


class Test_IP_Address(unittest.TestCase):
    def test_CommandLineInterface(self):
        command = ["echo", "hello world"]
        self.assertTrue(cli.commandLineInterface(command) == "hello world")
