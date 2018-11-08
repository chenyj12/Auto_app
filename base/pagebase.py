from base.logger import Logger

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

    def input(self, *doc, value):
        self.find_element(*doc).send_keys(*value)

    def swipLeft(driver, t=300, n=3):
        '''向左滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)
        logger.info('向左进行了滑动%s次' % n)
