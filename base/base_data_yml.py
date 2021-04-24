import yaml


# 读取data目录下的yaml格式数据
def base_data_yml(file_name):
    with open("./data/" + file_name + ".yml", "r", encoding="utf-8")as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data
        # print(data)
        # print(type(data))


if __name__ == "__main__":
    base_data_yml()
