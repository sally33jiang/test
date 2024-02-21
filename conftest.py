import pytest
import requests
import jsonpath
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/


def pytest_collect_file(parent, path):
    # 获取文件.yml 文件,匹配规则
    if path.ext == ".yml" and path.basename.startswith("test"):#这是一个条件判断语句，用于确定是否应该收集给定的文件。
        # print(path)#只有当文件既是.yml格式，并且其基本名以"test"开始时，这个条件才会为真。
        # print(parent)
        return YamlFile(path, parent)#如果上述条件为真，这行代码将返回一个新的YamlFile对象。YamlFile可能是一个自定义的类，用于处理或表示YAML格式的测试文件。



class YamlFile(pytest.File):
    # 读取文件内容
    def collect(self):
        import yaml
        raw = yaml.safe_load(self.fspath.open(encoding='utf-8'))# 解析yaml文件
        for yaml_case in raw:
            name = yaml_case["test"]["name"]#从当前YAML测试用例中提取name字段的值。这里假设每个测试用例都有一个test字段，而test字段下又有一个name子字段。
            values = yaml_case["test"]#提取当前YAML测试用例的test字段的所有值，并将其存储在values变量中。
            yield YamlTest(name, self, values)#用yield关键字生成一个新的YamlTest对象
# YamlFile类负责读取YAML格式的测试文件，并将其中的每个测试用例转换为一个YamlTest对象。这样，pytest就可以识别和执行这些测试用例了。#


class YamlTest(pytest.Item):
    def __init__(self, name, parent, values):
        super(YamlTest, self).__init__(name, parent)
        self.name = name
        self.values = values#这行代码将传入的 values 参数值赋给 YamlTest 对象的 values 属性
        self.request = self.values.get("request")
        self.validate = self.values.get("validate")
        self.s = requests.session()
#YamlTest 类用于表示从 YAML 文件中读取并解析出来的单个测试用例。它提取了测试用例的名称、原始数据以及其他可能需要的属性（如 request 和 validate），并准备了一个 requests 会话用于执行可能需要的 HTTP 请求。
    def runtest(self):
        # 运行用例
        request_data = self.values["request"]
        #这行代码从 self.values 字典中取出键为 "request" 的值，并将其存储在局部变量 request_data 中。
        # 这个 request_data 应该是一个字典，
        # 包含了执行 HTTP 请求所需的所有参数，如方法（method）、URL（url）、头信息（headers）、请求体（data 或 json）等
        # print(request_data)
        response = self.s.request(**request_data)
        print("\n", response.text)
        # 断言
        self.assert_response(response, self.validate)

    def assert_response(self, response, validate):
        '''设置断言'''
        import jsonpath
        for i in validate:
            if "eq" in i.keys():
                yaml_result = i.get("eq")[0]
                actual_result = jsonpath.jsonpath(response.json(), yaml_result)
                expect_result = i.get("eq")[1]
                print("实际结果：%s" % actual_result)
                print("期望结果：%s" % expect_result)
                assert actual_result[0] == expect_result

