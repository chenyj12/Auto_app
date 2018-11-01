from base.capability import driver,NoSuchElementException


meBtn=driver.find_element_by_id('com.example.homeking.client:id/va')


def login():
    driver.find_element_by_id('com.example.homeking.client:id/o4').click()
    driver.find_element_by_id('com.example.homeking.client:id/g9').send_keys('15060785807')
    driver.find_element_by_id('com.example.homeking.client:id/g8').send_keys('a147258')
    driver.find_element_by_id('com.example.homeking.client:id/zw').click()

try:
    meBtn.click()
    id=driver.find_element_by_id('com.example.homeking.client:id/a44').text
    print('已登录,用户ID为%s'%id)
except NoSuchElementException:
    print('未登录，点击登录')
    login()




