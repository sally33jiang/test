from selenium import webdriver
import pytest
import time
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/


@pytest.fixture(scope="module", name="driver")
def open_broswer():
    '''打开浏览器'''
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_blog(driver):
    '''打开我的blog: https://www.cnblogs.com/yoyoketang/'''
    driver.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(3)


@pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
def test():
    print("fixture初始化的参数列表")

# test_y.py

def test_h(home_url):
    print("用例：%s" % home_url)
