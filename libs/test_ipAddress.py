import unittest

import ipAddress as ip


class Test_IP_Address(unittest.TestCase):
    def test_CommandLineInterface(self):
        command = ["echo", "hello world"]
        self.assertTrue(ip.commandLineInterface(command) == "hello world")
