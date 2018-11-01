import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)
from base.capability import driver, NoSuchElementException


meBtn = driver.find_element_by_id('com.example.homeking.client:id/v5')


def login():
    driver.find_element_by_id('com.example.homeking.client:id/nx').click()
    driver.find_element_by_id('com.example.homeking.client:id/g9').send_keys('15060785807')
    driver.find_element_by_id('com.example.homeking.client:id/g8').send_keys('a147258')
    driver.find_element_by_id('com.example.homeking.client:id/zq').click()
    print('登录完成')

try:
    meBtn.click()
    id = driver.find_element_by_id('com.example.homeking.client:id/a40').text
    print('已登录,用户ID为%s' % id)
except NoSuchElementException:
    print('点击进行登录')
    login()
