from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'mi3',
    'platformVersion': '4.4.2',
    'noReset': True,
    'unicodeKeyboard': True,
    'appPackage': 'com.example.homeking.client',
    'appActivity': 'com.example.homeking.client.controllers.intro.IntroActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


def swipLeft(driver, t=500, n=2):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def check_wlcome():
    try:
        skipBtn = driver.find_element_by_id('com.example.homeking.client:id/a2p')
    except NoSuchElementException:
        print('已跳过欢迎页')
    else:
        swipLeft(driver)
        driver.find_element_by_id('com.example.homeking.client:id/z6').click()
        driver.find_element_by_xpath('//android.widget.CheckBox[@text=\"厦门\"]').click()


check_wlcome()
