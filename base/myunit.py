import unittest
from base.desired_caps import AppiumTest
from time import sleep
import warnings
import os


class startEnd(unittest.TestCase):


    def setUp(self):
        os.system('start appium')
        warnings.simplefilter("ignore",ResourceWarning)
        at=AppiumTest()
        self.driver = at.get_driver()

    def tearDown(self):
        sleep(2)
        self.driver.close_app()
