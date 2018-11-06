from selenium.webdriver.common.by import By
from base.pagebase import PageBase
from selenium.common.exceptions import NoSuchElementException


class Welcome(PageBase):
    sw = (By.ID, 'com.example.homeking.client:id/i5')
    expence = (By.ID, 'com.example.homeking.client:id/z0')
    citycode = (By.XPATH, '//android.widget.CheckBox[@text=\"厦门\"]')
    skipBtn = (By.ID, 'com.example.homeking.client:id/a2l')
    popBtn = (By.ID, 'com.example.homeking.client:id/is')

    def check_wlcome(self):
        try:
            sw1 = self.find_element(*self.sw)
            print('在欢迎页面引导页面')
            self.swipLeft()
            # self.swipLeft(self.driver)
            self.find_element(*self.expence).click()
            self.find_element(*self.citycode).click()
            self.check_pop()
        except NoSuchElementException:
            print('已初始化过')
        # else:
        #
        #     # self.check_ad()

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
            self.find_element(*self.popBtn).click()
            print('存在弹屏')
        except NoSuchElementException:
            print('没有弹屏')
