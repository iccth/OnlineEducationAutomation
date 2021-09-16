"""
    课程管理模块
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_object.login_page import LoginPage


class CoursePage(BasePage):
    # 核心元素
    url = 'http://edu.yuanzhangzcc.com/admin/#/course/course/course'
    course_name = (By.XPATH, '//label[@for="courseName"]/../div/div/input[@class="el-input__inner"]')
    search_button = (By.XPATH, '//span[contains(text(),"查询")]')

    # 核心流程一
    def search_classname(self, txt):
        self.visit()
        self.input_(self.course_name, txt)
        self.click(self.search_button)


# 调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    txt = '测试'
    cp = CoursePage(driver)
    cp.search_classname(txt)