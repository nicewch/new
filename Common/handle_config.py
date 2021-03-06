"""
#!/usr/bin/python3
coding : utf-8
Author :wangchunhong
Time   :2021/9/22 23:25
Project:api
"""

import os
from configparser import ConfigParser
from Common.handle_path import conf_dir

class HandleConfig(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        #继承解析类，读取文件
        self.read(file_path,encoding="utf-8")

file_path = os.path.join(conf_dir,"config.ini")#获取配置文件路径
conf = HandleConfig(file_path)

# if __name__ == '__main__':
#     conf = HandleConfig("config.ini")
#     conf.get('log','name')

