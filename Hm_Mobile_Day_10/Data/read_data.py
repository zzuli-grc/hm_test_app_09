import os
import yaml


def read_data():
    with open("/Users/liuhuajian/PycharmProjects/Hm_Mobile_Day_10/Data/data1.yaml", "r") as f:
        data = yaml.safe_load(f)
        print(data)


if __name__ == '__main__':
    read_data()
