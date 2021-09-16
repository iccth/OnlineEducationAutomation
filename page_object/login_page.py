"""
    登录页面
    主体:
        1.元素
            账号,密码,登录按钮
        2.业务
            用户登录行为
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):  # 引入基类模块
    # 核心元素
    url = 'http://edu.yuanzhangzcc.com/admin/#/login?redirect=%2Fdashboard'
    mobile = (By.NAME, 'mobile')
    password = (By.NAME, 'password')
    login_button = (By.XPATH, '//span[contains(text(),"登录")]')
    txt = (By.XPATH, '//*[contains(text(),"欢迎使用基点在线教育系统软件")]')

    # 核心业务流
    def login(self, mobile, pwd):
        self.visit()
        self.input_(self.mobile, mobile)
        self.input_(self.password, pwd)
        self.click(self.login_button)
        self.im_wait(10)
        # 添加一个返回值,用于获取断言的文本信息
        return self.driver.find_element_by_xpath('//*[contains(text(),"欢迎使用基点在线教育系统软件")]').text


# 调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    mobile = '18800000000'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(mobile, password)
