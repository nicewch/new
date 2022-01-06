# -*- coding: utf-8 -*-
# @Time      : 2022/1/5 16:10
# @Author    : wch
# @FileName  : Test_pay.py
# @Software  : PyCharm
import json
import unittest

from jsonpath import jsonpath

from Common.handle_data import replace_mark_with_data
from Common.handle_log import logger
from Common.handle_path import datas_dir
from Common.handle_phone import get_old_phone, get_new_phone
from Common.handle_requests import send_requests
from Common.myddt import ddt,data
from Common.handle_excel import HandleExcel
from Common.handle_config import conf
from Common.handle_db import HandleDB


he = HandleExcel(datas_dir + "\\api_cases.xlsx","充值")
cases =he.read_all_datas()  #读取数据文件所有数据
he.close_file()

db = HandleDB()  #连接数据库

@ddt
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  登录模块用例 开始执行  ========")
        # 前置条件，登录,得到用户id、token
        user, password = get_old_phone()
        resp = send_requests("POST","member/login",{"mobile_phone":user,"pwd":password})
        cls.menmber_id = jsonpath(resp.json(),'$.data.id')[0]
        cls.token = jsonpath(resp.json(),'$.data.token')[0]

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  登录模块用例 开始执行  ========")

    @data(*cases)
    def test_login(self,case):
        logger.info("*********   执行用例{}：{}   *********".format(case["id"], case["title"]))
        #替换数据
        if case["request_data"].find("#member_id#") != -1:
            case = replace_mark_with_data(case,"#member_id#",self.menmber_id)

        #通过数据库查询充值前当前账户的余额
        if case['check_sql']:
            before_count = db.select_one_data(case['check_sql'])['leave_amount']
            #充值的金额
            pay_money = json.load(case['request_data'])['amount']
            #充值后的金额 = 充值前的金额 + 充值金额
            after_money = 



