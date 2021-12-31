"""
#!/usr/bin/python3
coding : utf-8
Author :wangchunhong
Time   :2021/12/20 23:42
Project:api
"""


from openpyxl import load_workbook
import json


class HandleExcel:
    #初始化文件路径及表名
    def __init__(self,file_path,sheet_name):
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:  # 遍历第1行当中每一列
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        all_datas = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]:  # 遍历数据行
            values = []
            for val in item:  # 获取每一行的值
                values.append(val.value)
            res = dict(zip(titles, values))  # title和每一行数据，打包成字典
            all_datas.append(res)
        return all_datas  #返回列表，title和每一行测试数据组成的字典


    def close_file(self):
        self.wb.close()

if __name__ == '__main__':
    import os
    from Common.handle_path  import datas_dir
    file_path = os.path.join(datas_dir, "api_cases.xlsx")
    exc = HandleExcel(file_path,"注册")
    cases = exc.read_all_datas()
    exc.close_file()
    for case in cases:
        print(case)