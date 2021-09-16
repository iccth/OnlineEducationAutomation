"""基类
    常用函数:
    # 访问url
    # 元素定位
    # 输入
    # 点击
    # 等待
    # 关闭
    # ---
"""
from time import sleep

from selenium import webdriver


class BasePage:
    # 虚构driver对象
    driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def visit(self):
        self.driver.get(self.url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).clear()
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait(self, time_):
        sleep(time_)

    # 关闭
    def quit(self):
        self.driver.quit()

    # 隐式等待
    def im_wait(self, time_):
        self.driver.implicitly_wait(time_)
