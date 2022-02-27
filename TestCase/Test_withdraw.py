# -*- coding: utf-8 -*-
# @Time      : 2022/1/10 14:05
# @Author    : wch
# @FileName  : Test_withdraw.py
# @Software  : PyCharm


"""
提现接口：
   所有用例的前置：登陆！
                拿到2个数据：id，token
   把前置的数据，传递给到测试用例。

   充值接口的请求数据：id
             请求头：token

充值前的用户余额：{'leave_amount': Decimal('4536202.88')}
处理sql语句：把Decimal对应的字段值修改为字符串返回。CAST(字段名 AS CHAR)
select CAST(member.leave_amount AS CHAR) as leave_amount from member where id=#member_id#;
"""

import json
import unittest

from jsonpath import jsonpath

from Common.handle_data import replace_mark_with_data,EnvData
from Common.handle_log import logger
from Common.handle_path import datas_dir
from Common.handle_phone import get_old_phone
from Common.handle_requests import send_requests
from Common.myddt import ddt,data
from Common.handle_excel import HandleExcel
from Common.handle_db import HandleDB


he = HandleExcel(datas_dir+ "\\api_cases.xlsx","提现")
cases =he.read_all_datas()  #读取数据文件所有数据
he.close_file()

db = HandleDB()

@ddt
class Test_withdraw(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  提现模块用例 开始执行  ========")
        # 前置条件，登录,得到用户id、token
        user, password = get_old_phone()
        resp = send_requests("POST", "member/login", {"mobile_phone": user, "pwd": password})
        # cls.menmber_id = jsonpath(resp.json(),"$.data.id")[0]
        # cls.token = jsonpath(resp.json(),"$.data.token")[0]
        setattr(EnvData, "member_id", jsonpath(resp.json(), "$..id")[0])
        setattr(EnvData, "token", jsonpath(resp.json(), "$..token")[0])

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  提现模块用例 执行结束  ========")

    @data(*cases)
    def test_withdraw(self,case):
        logger.info("*********   执行用例{}：{}   *********".format(case["case_id"], case["title"]))
        # 开始提现前替换需要替换的用户id，包括请求、期望中的(str)
        if case["request_data"].find("#member_id#") != -1:
            case = replace_mark_with_data(case, "#member_id#", str(EnvData.member_id))

        #通过数据库查询提现前当前账户的余额
        if case['check_sql']:
            before_count = db.select_one_data(case['check_sql'])['leave_amount']  #before_count类型str
            logger.info("提现前的用户余额：{}".format(before_count))
            #提现的金额
            pay_money = json.loads(case["request_data"])["amount"]  #pay_money类型int
            logger.info("提现的金额为：{}".format(pay_money))
            #提现后的金额 = 提现前的金额 -提现金额  before_count转为float与int相加
            after_money = round(float(before_count) - pay_money,2)
            logger.info("期望的提现之后的金额为：{}".format(after_money))
            #替换期望结果中的预期金额(str)
            case = replace_mark_with_data(case,"#money#",str(after_money))

        #发起请求，提现
        resp = send_requests(case['method'],case['url'],case['request_data'],token = EnvData.token)

        #将期望结果转换成字典
        expected = json.loads(case['expected'])
        logger.info("期望结果是:{}".format(expected))

        try :
            self.assertEqual(resp.json()['code'],expected['code'])
            self.assertEqual(resp.json()['msg'], expected['msg'])
            if case['check_sql']:
                self.assertEqual(resp.json()['data']['id'], expected['data']['id'])
                self.assertEqual(resp.json()['data']['leave_amount'], expected['data']['leave_amount'])

                # 数据库查询当前余额str
                db_money = db.select_one_data(case['check_sql'])["leave_amount"]
                logger.info("提现后的用户余额：{}".format(db_money))
                # db_money是str需要转换成float，保留两位小数
                self.assertEqual("{:.2f}".format(expected["data"]["leave_amount"]), "{:.2f}".format(float(db_money)))
        except:
            raise

