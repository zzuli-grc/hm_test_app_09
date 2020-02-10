import allure
import pytest
from Base.get_yaml import GetYaml


def read_test_hm_data():
    my_list = []
    data = GetYaml().read_test_hm_data("data2.yml")
    for i in data.values():
        my_list.append(tuple(i.values()))
    print(my_list)
    return my_list


class TestHm(object):
    @pytest.mark.parametrize("a, b, c", read_test_hm_data())
    def test_01(self, a, b, c):
        assert a + b == c

    @allure.step("测试步骤")
    def test_02(self):
        allure.attach("txt文件名字", "txt文件内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_03(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_03(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_03(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_03(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_03(self):
        assert True
