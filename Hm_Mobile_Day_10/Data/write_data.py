import yaml


def write_data():
    data = {'Search_Data': {
        'search_test_002': {'expect': {'value': '你好'}, 'value': '你 好'},
        'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
    with open("./data3.yml", "a") as f:
        yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)


if __name__ == '__main__':
    write_data()
