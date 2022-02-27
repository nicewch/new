# -*- coding: utf-8 -*-
# @Time      : 2021/12/31 14:46
# @Author    : wch
# @FileName  : Test_login.py
# @Software  : PyCharm

import unittest

from Common.handle_data import replace_mark_with_data
from Common.handle_log import logger
from Common.handle_path import datas_dir
from Common.handle_phone import get_old_phone, get_new_phone
from Common.handle_requests import send_requests
from Common.myddt import ddt,data
from Common.handle_excel import HandleExcel
from Common.handle_config import conf


he = HandleExcel(datas_dir + "\\api_cases.xlsx","登录")
cases =he.read_all_datas()  #读取数据文件所有数据
he.close_file()


@ddt
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  登录模块用例 开始执行  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  登录模块用例 执行结束  ========")

    @data(*cases)
    def test_login(self,case):
        logger.info("*********   执行用例{}：{}   *********".format(case["id"], case["title"]))

        #phone, passwd = get_old_phone()
        #如果文件里有需要替换的数据，则读取mark替换
        if case["request_data"].find("#phone#") != -1:
            phone = conf.get("general_user","user")
            case = replace_mark_with_data(case,"#phone#",phone)

        resp = send_requests(case["method"], case["url"], case["request_data"])

        expected = eval(case["expected"])
        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            self.assertEqual(resp.json()['code'],expected['code'])
            self.assertEqual(resp.json()['msg'], expected['msg'])
        except AssertionError:
            logger.info('失败')
            raise






