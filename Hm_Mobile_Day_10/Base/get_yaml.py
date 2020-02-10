import os

import yaml


class GetYaml(object):

    def read_test_hm_data(self, yaml_name):
        with open("./Data" + os.sep + yaml_name, "r") as f:
            data = yaml.safe_load(f)
            return data
