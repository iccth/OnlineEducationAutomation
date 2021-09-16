# 测试用例
import re
import unittest
from time import sleep

from selenium import webdriver
from ddt import ddt, file_data, data

from page_object.course_manage.course_page import CoursePage
from page_object.login_page import LoginPage

@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.cp = CoursePage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/login.yaml')
    def test_1_login(self, mobile, password, ttt):
        txt = self.lp.login(mobile, password)
        sleep(1)
        self.assertEqual(txt, ttt)

    @data('小', 'Test', '学习')
    def test_2_search_classname(self, txt):
        self.cp.search_classname(txt)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
