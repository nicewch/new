"""
======================
Author: 柠檬班-小简
Time: 2020/6/29 21:12
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
"""
基于项目做定制化封装
1、鉴权:token
2、项目通用的请求头:
    {"X-Lemonban-Media-Type": "lemonban.v2"}
    
3、请求体格式：application/json
"""
import requests

def __handle_header(token=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param token: token值
    :return: 处理之后headers字典
    """
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type":"application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers

#
def send_requests(method,url,data=None,token=None):
    # 得到请求头
    headers = __handle_header(token)
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    if method == "GET":
        resp = requests.get(url,data,headers=headers)
    else:
        resp = requests.post(url,json=data,headers=headers)
    return resp


if __name__ == '__main__':
    login_url = "http://api.lemonban.com/futureloan/member/login"
    login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
    resp = send_requests("POST",login_url,login_datas)
    token = resp.json()["data"]["token_info"]["token"]

    recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    recharge_data = {"member_id": 200119, "amount": 2000}
    resp = send_requests("POST",recharge_url,recharge_data,token)
    print(resp.json())



