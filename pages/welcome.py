from selenium.webdriver.common.by import By
from base.pagebase import PageBase
from selenium.common.exceptions import NoSuchElementException
from base.logger import Logger

logger = Logger(logger="Welcome").getlog()


class Welcome(PageBase):
    sw = (By.ID, 'com.example.homeking.client:id/i5')
    expence = (By.ID, 'com.example.homeking.client:id/z0')
    citycode = (By.XPATH, '//android.widget.CheckBox[@text=\"厦门\"]')
    skipBtn = (By.ID, 'com.example.homeking.client:id/a2l')
    popBtn = (By.ID, 'com.example.homeking.client:id/is')

    def check_wlcome(self):
        try:
            sw1 = self.find_element(*self.sw)
            logger.info('在欢迎页面引导页面')
            self.swipLeft()
            self.click(*self.expence)
            self.click(*self.citycode)
            self.check_pop()
        except NoSuchElementException:
            self.check_pop()

    def check_ad(self):
        try:
            skipBtn = self.find_element(*self.skipBtn)
            print('存在广告图')
        except NoSuchElementException:
            print('开始点击跳过')
        else:
            skipBtn.click()

    def check_pop(self):
        try:
            self.click(*self.popBtn)
            logger.info('有弹屏广告，关闭广告图')
        except NoSuchElementException:
            logger.info('没有弹屏广告，不执行操作')
