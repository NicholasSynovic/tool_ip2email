import os
import unittest

import logger


class Test_Logger(unittest.TestCase):
    def test_createFile(self):
        testFile = logger.createFile()

        self.assertTrue(os.path.isfile(testFile))
        os.remove(testFile)

    def test(self):
        message = "Hello World"
        testFile = logger.createFile()
        logger.logToFile(message, testFile)

        def readFromFile(file) -> str:
            with open(file, "r") as testFile:
                return testFile.read()

        testFileData: str = readFromFile(testFile)

        self.assertTrue(testFileData.find(message) != -1)
