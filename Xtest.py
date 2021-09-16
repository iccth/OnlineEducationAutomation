# 供临时测试

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://192.168.1.200/admin/#/course/course/course')
driver.maximize_window()

driver.find_element_by_name('mobile').send_keys('18800000000')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_xpath('//span[contains(text(),"登录")]').click()
driver.implicitly_wait(10)

# 课程列表页面
driver.get('http://192.168.1.200/admin/#/course/course/course')
driver.find_element_by_xpath('//label[@for="courseName"]/../div/div/input[@class="el-input__inner"]').send_keys('ceshi')