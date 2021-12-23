"""
======================
Author: 柠檬班-小简
Time: 2020/6/29 14:49
Project: 接口自动化备课代码
Company: 湖南零檬信息技术有限公司
======================
"""
"""
课堂派案例

课堂派是以cookies方式来鉴权的。
========== 第一步：登陆课堂派，获取cookies。============
登陆url: https://www.ketangpai.com/UserApi/login
请求类型：post
请求体格式：application/x-www-form-urlencoded
请求数据：
    datas = {"email":"2501768591@qq.com",
             "password":"nmb_python",
             "remember":0}

响应结果：
{"status":1,"url":"\/Main\/index.html","token":"MDAwMDAwMDAwMMurrpWavLehhs1-mbKpfZSEzX_NfXV7qcRr2Z97n6Gas4Wt14LStKuYu4vZyKykzH_Nodx9dXuaxaa3m5Z8iGHHiZXQgs_VsIW4oN6yqYHahN2LlpeDbm0","isenterprise":0,"uid":"MDAwMDAwMDAwMLWGtdyH37-y"}
cookies在响应头当中，有一个set-cookie

========== 第二步：获取用户信息 ============
接口url: https://www.ketangpai.com/UserApi/getUserInfo
请求方法：get
请求参数：无

"""
"""
Session类：创建一个会话对象。
"""
import requests
# # 第一步 实例化Session对象
# s = requests.Session()
#
# print("登陆之前的cookies:",s.cookies)
#
# # 第二步 - 登陆，得到cookies鉴权。
login_url = "https://www.ketangpai.com/UserApi/login"
login_datas = {"email":"2501768591@qq.com",
             "password":"nmb_python",
             "remember":0}
# response = s.post(login_url,data=login_datas)
# # print("登陆响应的cookies: ",response.cookies)
#
# print("登陆之后的cookies:",s.cookies) # 主动会将响应的set-cookies添加到s对象当中。
#



# # 第二种方式：自己主动获取 cookies，并在后续的请求当中，主动加上cookies
# # # 第二步：获取用户信息
# userinfo_url = "https://www.ketangpai.com/UserApi/getUserInfo"
# # resp = s.get(userinfo_url)
# # print(resp.json())
#
# # 第一步 - 登陆，得到cookies鉴权。
# resp = requests.post(login_url,data=login_datas)
# # 主动获取cookie
# cookies = resp.cookies
# # print(cookies)
#
# # 第二步： 获取 用户信息
# resp = requests.get(userinfo_url,cookies=cookies)
# print(resp.json())
