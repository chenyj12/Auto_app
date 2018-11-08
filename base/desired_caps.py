import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)
from appium import webdriver

# 获取项目的根目录路径a
p = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# 获取app路径
appPath = lambda x: os.path.join(p, "app", x)


class AppiumTest:
    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'mi3',
            'platformVersion': '4.4.2',
            'app': appPath("2.9.5.apk"),
            'noReset': False,
            'unicodeKeyboard': True,
            'appPackage': 'com.example.homeking.client',
            'appActivity': 'com.example.homeking.client.controllers.intro.IntroActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(6)

    def get_driver(self):
        return self.driver
