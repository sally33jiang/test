import pytest

# 调用方式一
@pytest.fixture
def login():
    print("输入账号，密码先登录")
def test_s1(login):  #迭代器
    print("用例 1：登录之后其它动作 111")
def test_s2():  # 不传 login
    print("用例 2：不需要登录，操作 222")
# 调用方式二
@pytest.fixture
def login2():
    print("please输入账号，密码先登录")
@pytest.mark.usefixtures("login2", "login") # login2 函数 和login函数都会使用
def test_s11():
    print("用例 11：登录之后其它动作 111")
# 调用方式三
@pytest.fixture(autouse=True)
def login3():
    print("====auto===")
# 不是test开头，加了装饰器也不会执行fixture
@pytest.mark.usefixtures("login2")
def loginss():
    print(123)