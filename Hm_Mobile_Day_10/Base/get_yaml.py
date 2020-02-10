import os

import yaml
from utils import BASE_DIR


class GetYaml(object):

    def read_test_hm_data(self, yaml_name):
        with open(BASE_DIR + "/Data" + os.sep + yaml_name, "r") as f:
            data = yaml.safe_load(f)
            return data


print(BASE_DIR)
