"""
#!/usr/bin/python3
coding : utf-8
Author :wangchunhong
Time   :2021/12/26 23:36
Project:api
"""


"""
1、数据库连接 conn  cur
2、获取一条数据？
3、获取条数
4、获取所有的数据
5、关闭数据库连接
"""
import pymysql

from Common.handle_config import conf

class HandleDB:

    def __init__(self):
        # 连接数据库，创建游标。
        # 1、建立连接
        self.conn = pymysql.connect(
            host=conf.get("mysql","host"),
            port=conf.getint("mysql","port"),
            user=conf.get("mysql","user"),
            password=conf.get("mysql","password"),
            database=conf.get("mysql","database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor #指定查询结果后返回数据的类型为字典
        )
        # 2、创建游标
        self.cur = self.conn.cursor()

    def select_one_data(self,sql):
        self.conn.commit()  #提交同步数据
        self.cur.execute(sql)   #执行sql语句
        return self.cur.fetchone()  #获取sql语句 执行后的一条数据结果

    def select_all_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        self.conn.commit()
        return self.cur.execute(sql) #返回sql语句执行结果的行数

    def update(self,sql):
        """
        对数据库进行增、删、改的操作。
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    # sql = 'select * from member LIMIT 3'
    # db = HandleDB()
    # count = db.get_count(sql)
    # print("结果个数为：",count)
    # data = db.select_one_data(sql)
    # print("一条数据：",data)
    # all = db.select_all_data(sql)
    # print("所有的数据：",all)
    # db.close()
    # 初始化数据库对象
    db = HandleDB()
    sql = 'select * from member where mobile_phone="18600001120"'
    # 发起一个注册请求
    from Common.handle_requests import send_requests
    case = {
        "method":"POST",
        "url":"http://api.lemonban.com/futureloan/member/register",
        "request_data":{"mobile_phone":"18600001120","pwd":"123456789","type":1,"reg_name":"美丽可爱的小简"}
    }
    response = send_requests(case["method"], case["url"], case["request_data"]) # 接口
    print("响应结果：",response.json())
    # 查询注册的手机号码
    count = db.get_count(sql)
    print("获取到的结果为：",count)
