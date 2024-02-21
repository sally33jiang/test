'''
request 是 pytest的内置fixture
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/
'''
import pytest

# 测试数据
test_data = ["user1", "user2"]


@pytest.fixture(params=test_data)
def register_users(request):
     # 获取当前的测试数据
     user = request.param
     print(user)
     print("\n拿着这个账号去注册：%s"%user)
     result = "success"
     return user, result


def test_register(register_users):
    user, result = register_users
    print("在测试用例里面里面获取到当前测试数据：%s"%user)
    print(result)
    assert result == "success"
