# 测试用例
import unittest

from selenium import webdriver

from page_object.login_page import LoginPage
from page_object.course_manage.course_page import CoursePage


class TestSearchCourse():
    def test_searchby_cname(self):
        driver = webdriver.Chrome()
        mobile = '188000000000'
        password = '123456'
        txt = '测试'
        lp = LoginPage(driver)
        lp.login(mobile, password)
        cp = CoursePage(driver)
        cp.search_classname(txt)


if __name__ == '__main__':
    unittest.main()
    # pytest.main(['-vs', 'test_course_search.py'])
