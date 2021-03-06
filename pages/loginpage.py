from selenium.webdriver.common.by import By
from base.pagebase import PageBase
from selenium.common.exceptions import NoSuchElementException
from base.logger import Logger
from time import sleep


logger = Logger(logger="LoginPage").getlog()


class LoginPage(PageBase):
    # 登录相关控件
    passlogin = (By.ID, 'com.example.homeking.client:id/nx')
    phone = (By.ID, 'com.example.homeking.client:id/g9')
    passw = (By.ID, 'com.example.homeking.client:id/g8')
    loginbtn = (By.ID, 'com.example.homeking.client:id/zq')
    meBtn = (By.ID, 'com.example.homeking.client:id/v5')
    id = (By.ID, 'com.example.homeking.client:id/a40')
    # 欢迎页相关控件
    sw = (By.ID, 'com.example.homeking.client:id/i5')
    expence = (By.ID, 'com.example.homeking.client:id/z0')
    citycode = (By.XPATH, '//android.widget.CheckBox[@text=\"广州\"]')
    skipBtn = (By.ID, 'com.example.homeking.client:id/a2l')
    popBtn = (By.ID, 'com.example.homeking.client:id/is')
    # 退出相关控件
    setting = (By.ID, 'com.example.homeking.client:id/u0')
    lgoinout = (By.ID, 'com.example.homeking.client:id/zr')
    queding = (By.ID, 'com.example.homeking.client:id/d1')
    #权限允许
    allows = (By.ID, 'android:id/button1')

    def login_out(self):
        sleep(2)
        logger.info('-----退出账号操作-----')
        self.swipToElement(*self.setting)
        self.click(*self.lgoinout)
        self.click(*self.queding)

    def check_wlcome(self):
        logger.info('-----检查是否在欢迎引导页面-----')
        self.alawys_allow()
        try:
            sw1 = self.find_element(*self.sw)
            logger.info('在欢迎页面引导页面')
            self.swipLeft()
            self.click(*self.expence)
            sleep(2)
            self.click(*self.citycode)
            sleep(5)
            self.check_pop()
        except NoSuchElementException:
            self.check_pop()

    def check_ad(self):
        logger.info('-----检查是否有广告图-----')
        try:
            skipBtn = self.find_element(*self.skipBtn)
            print('存在广告图')
        except NoSuchElementException:
            print('开始点击跳过')
        else:
            skipBtn.click()

    def check_pop(self):
        logger.info('-----检查是否有弹屏广告-----')
        try:
            self.click(*self.popBtn)
            logger.info('有弹屏广告，关闭广告图')
        except NoSuchElementException:
            logger.info('没有弹屏广告，不执行操作')

    def login(self, username, password):
        self.check_wlcome()
        try:
            self.click(*self.meBtn)
            id = self.find_element(*self.id).text
            logger.info('已登录,用户ID为%s' % id)
        except NoSuchElementException:
            logger.info('-----开始执行登录操作------')
            self.click(*self.passlogin)
            logger.info('输入的用户名：%s'%username)
            self.find_element(*self.phone).send_keys(username)
            logger.info('输入的密码：%s' % password)
            self.find_element(*self.passw).send_keys(password)
            sleep(1)
            self.click(*self.loginbtn)

    def check_loginStatus(self):
        logger.info('-----检查登录状态-----')
        try:
            self.click(*self.meBtn)
            id = self.find_element(*self.id).text
            logger.info('已登录,用户ID为%s' % id)
        except NoSuchElementException:
            logger.error('登录失败')
            self.getScreenShot('login fail')
            return False
        else:
            logger.info('登录成功!')
            self.login_out()
            return True

    def alawys_allow(self, number=2):
        logger.info('-----检查是否存在权限确认-----')
        for i in range(number):
            try:
                self.click(*self.allows)
            except:
                pass
