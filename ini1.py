

import pytest
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/

@pytest.fixture
def a():
    return 'a'


@pytest.fixture
def b():
    return 'b'


@pytest.fixture(params=['a', 'b'])
def arg(request):
    return request.getfixturevalue(request.param)
    a=request.getfixturevalue(request.param)
    print(a)

#通过 request.getfixturevalue(“fixture name”) 方法来获取fixture的返回值




def test_foo(arg):
    assert len(arg) == 1
