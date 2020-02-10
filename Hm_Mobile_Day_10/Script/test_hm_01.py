import pytest
import yaml
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


if __name__ == '__main__':
    read_test_hm_data()
