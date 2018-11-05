import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 获取项目的根目录路径a
p = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# 获取app路径
appPath = lambda x: os.path.join(p, "app", x)

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

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(6)


def swipLeft(driver, t=2000, n=3):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
    print('向左滑动')


def check_pop():
    try:
        popBtn = driver.find_element_by_id('com.example.homeking.client:id/is')
        popBtn.click()
        print('存在弹屏')
    except NoSuchElementException:
        print('没有弹屏')


def check_wlcome():
    try:
        sw = driver.find_element_by_id('com.example.homeking.client:id/i5')
        print('在欢迎页面引导页面')

    except NoSuchElementException:
        print('已跳过欢迎页')
    else:
        swipLeft(driver)
        driver.find_element_by_id('com.example.homeking.client:id/z0').click()
        driver.find_element_by_xpath('//android.widget.CheckBox[@text=\"厦门\"]').click()
        check_p()
        check_pop()


def check_p():
    try:
        skipBtn = driver.find_element_by_id('com.example.homeking.client:id/a2l')
        print('存在广告图')
    except NoSuchElementException:
        print('开始点击跳过')
    else:
        skipBtn.click()


check_wlcome()
driver.find_element_by_id('com.example.homeking.client:id/jk').click()

aa = driver.context
print(aa)
driver.press_keycode(4)
