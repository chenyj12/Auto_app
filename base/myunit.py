import unittest
from base.desired_caps import AppiumTest
from time import sleep
import warnings


class startEnd(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        at=AppiumTest()
        self.driver = at.get_driver()

    def tearDown(self):
        sleep(5)
        self.driver.close_app()
