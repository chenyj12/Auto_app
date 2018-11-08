import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)
from base import myunit
from pages.loginpage import LoginPage
from pages.welcome import Welcome
import unittest


class TestLogin(myunit.startEnd):

    def test03(self):
        '''
        账号密码正确
        '''
        we = Welcome(self.driver)
        we.check_wlcome()
        lo = LoginPage(self.driver)
        lo.login('15060785807', 'a147258')

    def test02(self):
        '''
        账号或密码错误
        '''

        we = Welcome(self.driver)
        we.check_wlcome()
        lo = LoginPage(self.driver)
        lo.login('15060785807a', 'a147258')

    def test01(self):
        '''
        账号或密码为空
        '''
        we = Welcome(self.driver)
        we.check_wlcome()
        lo = LoginPage(self.driver)
        lo.login('', '')


if __name__ == '__main__':
    unittest.main()
