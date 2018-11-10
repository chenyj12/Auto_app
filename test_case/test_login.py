import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)
from base import myunit
from pages.loginpage import LoginPage
import unittest


class TestLogin(myunit.startEnd):

    def test03(self):
        '''账号密码输入正确'''
        lo = LoginPage(self.driver)
        lo.login('15060785807', 'a147258')
        self.assertTrue(lo.check_loginStatus())

    def test02(self):
        '''账号或密码输入错误'''
        lo = LoginPage(self.driver)
        lo.login('15060785807', 'a11147258')
        self.assertFalse(lo.check_loginStatus(), msg='登录失败')

    def test01(self):
        ''' 账号或密码输入为空'''
        lo = LoginPage(self.driver)
        lo.login('150', '')
        self.assertFalse(lo.check_loginStatus(), msg='登录失败')

if __name__ == '__main__':
    unittest.main()
