# coding:utf-8

import os
import sys
import time
import requests


now = time.strftime('%Y-%m-%d %H:%M')
# print(now)
#
# sql = "2018-08-30 14:40"
#
# if sql == now:
#     print(True)
# else:
#     print(False)


url = "http://apigw-dev.veehui.com/api/v1/u/userStatistics"
URL = "http://apigw-dev.veehui.com/api/v1/m/liveOrPreviewMeetingCount"

headers = {"Content-Type":"application/json"
        # "Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJvMVdWWnd6WW9IZTE1cFVtQk5ydWZLXzJzclU0IiwiZXhwIjoxNTM4NzkxOTcyLCJpYXQiOjE1MzYxOTk5NzJ9.PtqFgmpodwkaXpE_lcqcn66w3E32fPrehseKzORGAxQ-jwbfW-zkMjkYIGlscCxeaW5cdpI5i7Fj9KOaNfIgcw"
            }

params =  {"startTime" : "2018-01-01 00:00:00","endTime" : "2018-12-31 23:59:59"}
# params = {}
result = requests.request("POST",URL,json=params,headers = headers)

print(result.json())






#
# # coding:utf-8
#
# import requests
# from HuShi.Common.readData import Read_Data
# from HuShi.Common.readData_DDT import Read_Data_ddt
# from HuShi.Common.logger import Logging
# from HuShi.Common.package_params import Parameter
# from HuShi.Config.env_config import Environment
# from HuShi.Common.writeReport import WriteReport
# from HuShi.Common.keyIssue import KeyIssue
# from HuShi.Common.conn_mysql import Conn_MySQL
# import HuShi.Config.params_config
# import unittest
# import os
# import time
# import ddt
#
# data_ddt = Read_Data_ddt("test_data_ddt.xlsx").Get_Data()
#
# @ddt.ddt
# class test_Requests(unittest.TestCase):
#
#     def __init__(self,method):
#         super(test_Requests, self).__init__(method)
#         self.headers = HuShi.Config.params_config.headers
#
#     @ddt.data(*data_ddt)
#     def test_requests(self,data):
#
#         WriteReport().Creat_Report()
#         url = Environment().Test() + data["api"]
#
#         # 请求
#         result = requests.request(data["method"],url,json=eval(data["params"]),headers=self.headers)
#         Logging().Info("<请求:\t" + url +">\t<参数:" + data["params"] +">\t<结果:"+ result.text)
#         # 当前时间
#         now = time.strftime('%Y-%m-%d %H:%M')
#         # 获取报告行数
#         n = WriteReport().Get_MaxRow()
#
#         # 判断是否需要SQL校验
#         if int(data["is_check"]) == int(1):
#             # 链接数据库，查询比对数据
#             SQL_check_data = Conn_MySQL().Connect(data["SQL_check"])
#             try:
#                 assert int(data["check_data"]) == int(SQL_check_data)
#             except:
#                 WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], str(SQL_check_data), result.text)
#                 # Jira提交BUG
#                 # KeyIssue().Commit(data["api"],data["params"],result.text,str(check_data),1,sql=data["check"])
#                 error_info = "【断言错误】\t<验证值：" + str(SQL_check_data) + "\t<Response:\t" + result.text + ">"
#                 Logging().Error(error_info)
#                 raise
#
#         elif int(data["is_check"]) == int(2):
#             # 链接数据库，查询比对数据
#             SQL_check_data = Conn_MySQL().Connect(data["SQL_check"])
#             try:
#                 assert str(SQL_check_data["result"]) == str(result.json()["result"][data["check_data"]])
#             except:
#                 WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], str(result.json()["result"][data["check_data"]]), result.text)
#                 # Jira提交BUG
#                 # KeyIssue().Commit(data["api"],data["params"],result.text,str(check_data),1,sql=data["check"])
#                 error_info = "【断言错误】\t<验证值：" + str(result.json()["result"][data["check_data"]]) + "\t<Response:\t" + result.text + ">"
#                 Logging().Error(error_info)
#                 raise
#
#         else:
#             try:
#                 assert result.json()["code"] == str(data["code"])
#             except:
#                 # 断言错误报告
#                 WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], data["code"], result.text)
#                 # Jira提交BUG
#                 # KeyIssue().Commit(data["api"], data["params"], result.text, data["code"], 0)
#                 error_info = "【断言错误】\t<正确状态码："+ str(data["code"]) +"\t<Response:\t" + result.text + ">"
#                 Logging().Error(error_info)
#                 raise
#
# if __name__ == "__main__":
#
#     unittest.main()
#     # 正则匹配 .*"id":(/d*).*