"""
======================
Author: 柠檬班-小简
Time: 2020/7/15 20:05
Project: day8
Company: 湖南零檬信息技术有限公司
======================
"""


"""
字符串：正则表达式
http://www.lemfix.com/topics/393
https://www.cnblogs.com/Simple-Small/p/9150947.html

字符串匹配、提取
regular

正则表达式手册：https://tool.oschina.net/uploads/apidocs/jquery/regexp.html

单个匹配表达式
.	匹配除“\n”之外的任何单个字符
\d	匹配一个数字字符。等价于[0-9]。
\D	匹配一个非数字字符。等价于[^0-9]
\w	匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”。
\W	匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
[xyz]  字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”
[a-z] 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
x|y  匹配x或者y

数量上的匹配：
{m}  n是一个非负整数。匹配前一个字符的n次
{n,m} 匹配前一个字符至少n次，最多m次
{n,} 匹配前一个字符至少n次

*  匹配前一个字符，0次或多次。
+  匹配前一个字符，1次或多次。
?  匹配前一个字符，0次或1次。

贪婪模式：尽可能匹配更多更长。默认的贪婪模式。
非贪婪模式：尽可能匹配更少。
    改成非贪婪模式，在限定数量表达式后面加上?

边界字符
^ 	匹配输入字符串的开始位置。
$   匹配输入字符串的结束位置。

   ？ 当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
   非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。
   例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”。

4、多选项匹配
   | 匹配多个规范   x|y  匹配x或者y
   [zxy]  匹配zxy中的任意字符
   [a-z]  匹配a-z范围内的任意字符  比如[0-9][a-z][A-Z]
   
5、() 匹配分组：将括号里的匹配出来


"""
import re

s = "sdk11fj12333445fga000000009abcdffda111a%^&*=---柠檬班。sfsfd"
data = '{"member_id": #member_id#,"amount":600,money:#user_money#,username:"#user#"}'

res = re.findall("#(.*?)#",data)
print(res)

# ()提取
# res = re.findall("a(\d+)a",s)
# print(res)

# res = re.findall("a(.*?)a",s)
# print(res)

# 数量上的匹配：
# res = re.findall("\d+",s)
# print(res)
# res = re.findall("1.*",s)
# print(res)
# res = re.findall("^[a-z]+",s)
# print(res)
# res = re.findall("[a-z]$",s)
# print(res)

# res = re.findall("\d{3,5}",s)
# print(res)
# res = re.findall("\d{3,5}?",s)
# print(res)
# res = re.findall("\d{3,}",s)
# print(res)
# res = re.findall("\d{3}",s)
# print(res)


# 单字符匹配
# res = re.findall(".",s)
# print(res)
# res = re.findall("\d",s)
# print(res)
# res = re.findall("\D",s)
# print(res)
# res = re.findall("\W",s)
# print(res)
# res = re.findall("[abcd]",s)
# print(res)
# res = re.findall("[A-Za-z0-9]",s)
# print(res)
# res = re.findall("abc|123|11",s)
# print(res)

import re

# case = {
#         "method": "POST",
#         "url": "http://api.lemonban.com/futureloan/member/register",
#         "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "#nick#"}'
#     }
#
# res = re.findall("#.*?#",case["request_data"])
# print(res)


resp = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 200713,
        "leave_amount": 4000.0,
        "mobile_phone": "18605671115",
        "reg_name": "美丽可爱的小简",
        "reg_time": "2020-06-29 11:52:20.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2020-07-06 21:48:53",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDcxMywiZXhwIjoxNTk0MDQzMzMzfQ.WJMI0-t7YZD8FtAiaYR8-SH1p58_7fJjnvS6xVw7_hYTe7eVIyxj3W2Oj7SlwR8dDZBc1T59U2ngRROXyFjx_Q"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}

import json

res_str = json.dumps(resp)
print(res_str)


# res = re.findall('"token":(.*?)}',res_str)
# print(res)

ss = "**abcdeefdg123345233"
# result = re.findall("\W",s)
# print(result)

# result = re.findall("[0-9]+?",s)
# print(result)

strs = '{"loan_id":#loan_id#,"approved_or_not": True,"member":#member_id#}'
# result = re.search("#(.*?)#",strs)
# print(result)
# res = result.group(1)
# print(res)

print("888888888888888888888888888888888888")
# result = re.search("#(.*?)#",strs)
# print(result)
# res = result.group(1)
# print(res)


