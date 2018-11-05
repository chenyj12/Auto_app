from selenium.webdriver.common.by import By
from base.pagebase import PageBase
from selenium.common.exceptions import NoSuchElementException


class LoginPage(PageBase):
    passlogin = (By.ID, 'com.example.homeking.client:id/nx')
    phone = (By.ID, 'com.example.homeking.client:id/g9')
    passw = (By.ID, 'com.example.homeking.client:id/g8')
    loginbtn = (By.ID, 'com.example.homeking.client:id/zq')
    meBtn = (By.ID, 'com.example.homeking.client:id/v5')
    id = (By.ID, 'com.example.homeking.client:id/a40')

    def login(self, phones, paw):
        try:
            self.find_element(*self.meBtn).click()
            id = self.find_element(*self.id).text
            print('已登录,用户ID为%s' % id)
        except NoSuchElementException:
            print('点击进行登录')
            self.find_element(*self.passlogin).click()
            self.find_element(*self.phone).send_keys(phones)
            self.find_element(*self.passw).send_keys(paw)
            self.find_element(*self.loginbtn).click()
            print('登录完成')

