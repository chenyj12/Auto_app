from base.logger import Logger
import os
import time

logger = Logger(logger="PageBase").getlog()


class PageBase(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *doc):
        return self.driver.find_element(*doc)

    def find_elements(self, *doc):
        return self.driver.find_element(*doc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, stat_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(stat_x, start_y, end_x, end_y, duration)

    def click(self, *doc):
        self.find_element(*doc).click()

    def swipLeft(driver, t=300, n=3):
        '''向左滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)
        logger.info('向左进行了滑动%s次' % n)

    def swipDown(driver):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        driver.swipe(x1, y1, x1, y2, 500)

    def swipToElement(self, *doc):
        try:
            self.find_element(*doc).click()
        except Exception as e:
            self.swipDown()
            self.find_element(*doc).click()

    def getScreenShot(self,modle):
        screens_dir = 'F:\\Auto_app\\test_result\\screenshots'
        now = time.strftime('%Y-%m-%d-%H_%M_%S')
        file_name = screens_dir + '/'+now + '%s.png'% modle
        logger.info('-----进行截图操作-----')
        self.driver.get_screenshot_as_file(file_name)

    def getTime(self):
        tamp = int(time.time())
        return tamp
