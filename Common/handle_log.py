"""
#!/usr/bin/python3
coding : utf-8
Author :wangchunhong
Time   :2021/9/21 23:44
Project:api
"""
import logging
import os

from Common.handle_config import conf
from Common.handle_path import logs_dir

class mylogger(logging.Logger):
    def __init__(self,file = None):
        # 设置输出级别、输出渠道、输出日志格式，继承Logger默认的日志收集器root
        super().__init__(conf.get("log","name"),conf.get("log","level"))

        #设置渠道的输入内容日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # 设置日志输出在控制台渠道
        handle1 = logging.StreamHandler()
        # 将日志格式绑定到渠道当中
        handle1.setFormatter(formatter)
        # 将设置好的渠道，添加到日志收集器上
        self.addHandler(handle1)

        if file:
            #文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

# 是否需要写入文件file_ok=true
if conf.getboolean("log","file_ok"):
    file_name = os.path.join(logs_dir,conf.get("log","file_name"))

else:
    file_name = None

logger = mylogger(file_name)

#logger.info("1111111111111111")