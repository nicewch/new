"""
#!/usr/bin/python3
coding : utf-8
Author :wangchunhong
Time   :2021/12/28 22:08
Project:api
"""

import json
import re
import jsonpath
from Common.handle_config import conf

"""
1、一条用例涉及到数据当中，有url、request_data、check_sql

"""



class EnvData:
    """
    存储用例要使用到的数据。环境变量的名称必须与标识符一致
    """
    pass

def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)



def replace_case_by_regular(case):
    """
    :param case: excel当中，读取的整条case（字典，字典里面的值是字符串），但凡有标识符，做全部替换
    包括url,request_data,expected,check_sql
    :return:
    """
    for key,value in case.items():
        if value is not None and isinstance(value, str):  # 确保value是个字符串
            case[key] = replace_by_regular(value) #将value替换
    return case

    # 把case字典(从excel读取出来的一条用例数据)转换成字符串
    # case_str = json.dumps(case)
    # # 替换
    # new_case = replace_by_regular(case_str)
    # # 把替换的的字符串，转换成字典。
    # case_dict = json.loads(new_case)
    # return case_dict



def replace_by_regular(data):
    """
    将字符串data匹配#(.*?)#的部分，替换对应的标识符对应的值
    标识符对应的值：1.conf中的data  2.设置为EvnData环境变量的类属性（必须都是字符串类型）
    :param data: 字符串
    :return: 返回替换之后的字符串
    """
    res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表。
    if res:
        for item in res:   #遍历标识符
            # 根据标识符res到环境变量/配置文件 中找到标识符res对应的值
            try:
                value = conf.get("data", item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    # value = "#{}#".format(item)
                    continue
            #print(value)
            # 将字符串中不同的标识符替换为对应的值
            data = data.replace("#{}#".format(item), value)
    return data


def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值#
    real_data: 要替换mark的真实数据。
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case

if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    }
    if case["request_data"].find("#phone#") != -1:
        case = replace_mark_with_data(case, "#phone#", "123456789001")
    c = json.loads(case.get("request_data"))
    c = jsonpath.jsonpath(c,"$.mobile_phone")
    print(c)
    for key,value in case.items():
        print(key,value)
