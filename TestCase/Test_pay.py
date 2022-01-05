# -*- coding: utf-8 -*-
# @Time      : 2022/1/5 16:10
# @Author    : wch
# @FileName  : Test_pay.py
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


he = HandleExcel(datas_dir + "\\api_cases.xlsx","充值")
cases =he.read_all_datas()  #读取数据文件所有数据
he.close_file()


@ddt
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  登录模块用例 开始执行  ========")
        # 前置条件，登录,得到用户id、token
        user, password = get_old_phone()
        resp = send_requests("POST","member/login",{"mobile_phone":user,"pwd":password})


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  登录模块用例 开始执行  ========")

    @data(*cases)
    def test_login(self,case):
        logger.info("*********   执行用例{}：{}   *********".format(case["id"], case["title"]))
        #替换数据
        if case["request_data"].find("#phone#") != -1:

            case = replace_mark_with_data(case,"#phone#",phone)
