"""
#!/usr/bin/python3
coding : utf-8
Author :wangchunhong
Time   :2021/12/22 21:52
Project:api
"""


import unittest
import os

from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.myddt import ddt,data
from Common.handle_path import datas_dir
from Common.handle_log import logger


he = HandleExcel(datas_dir + "\\api_cases.xlsx","注册")
cases = he.read_all_datas()  #读取测试数据
he.close_file()

@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  注册模块用例 开始执行  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  注册模块用例 执行结束  ========")


    @data(*cases)
    #注册接口
    def test_register_ok(self,case):
        logger.info("*********   执行用例{}：{}   *********".format(case["id"],case["title"]))
        expected = eval(case["expected"])  #期望字符串转换为字典
        # 步骤 测试数据 - 发起请求
        response = send_requests(case["method"],case["url"],case["request_data"])
        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            self.assertEqual(response.json()["code"],expected["code"]) #断言响应code与期望code
            self.assertEqual(response.json()["msg"], expected["msg"])
            assert True
        except AssertionError:
            logger.exception("断言失败！")
            assert False

