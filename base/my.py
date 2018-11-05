import unittest
from base.cap_base import AppiumTest
from time import sleep


class startEnd(unittest.TestCase):

    def setUp(self):
        at=AppiumTest()
        self.driver = at.get_driver()

    def tearDown(self):
        sleep(5)
        self.driver.close_app()
