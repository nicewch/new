"""
======================
Author: 柠檬班-小简
Time: 2020/6/29 14:50
Project: 接口自动化备课代码
Company: 湖南零檬信息技术有限公司
======================
"""
"""
第一步：获取登陆请求返回当中的token值。
第二步：拿着第一步的token值，去发送其它的请求。
注意：每一次登陆生成的token都不一样。再次登陆后，上一次的token就直接失效。以最新的token为准

前程贷项目，标准请求头要求：
 headers = {"X-Lemonban-Media-Type": "lemonban.v2",
                    "Content-Type": "application/json"}

========== 第一步：登陆前程贷，获取token值============
登陆url: url = "http://api.lemonban.com/futureloan/member/login"
请求类型：post
请求数据：
    datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}

响应数据中获取token值：token = resp.json()["data"]["token_info"]["token"]


========== 第二步：给上一步用户进行充值操作，请求头当中，Authorization中设置为Bearer {token}============
充值url：http://api.lemonban.com/futureloan/member/recharge
请求类型：post
请求数据：datas = {"member_id": 200119, "amount": 2000}
"""
import requests


headers = {"X-Lemonban-Media-Type": "lemonban.v2"}

# 第一步：登陆，拿token
login_url = "http://api.lemonban.com/futureloan/member/login"
login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
resp = requests.post(login_url,json=login_datas,headers=headers)
# for key,value in resp.json().items():
#     print(key,value)
resp_dict = resp.json()
print(resp_dict)
token = resp_dict["data"]["token_info"]["token"]
member_id = resp_dict["data"]["id"]
print(token)

# 第二步：充值。将token添加请求头当中： Authorization：Bearer token值
headers["Authorization"] = "Bearer {}".format(token)
print(headers)
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
recharge_data = {"member_id": member_id, "amount": 2000}
resp = requests.post(recharge_url,json=recharge_data,headers=headers)
print(resp.json())