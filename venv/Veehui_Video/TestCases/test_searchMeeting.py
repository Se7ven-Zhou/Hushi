# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
import HuShi.Config.params_config
import unittest
import pytest
import os
import time


class test_SearchMeeting(unittest.TestCase):

    def __init__(self,methodName):

        super(test_SearchMeeting, self).__init__(methodName)

        self.api = "/meeting/search"
        self.signature = HuShi.Config.params_config.signature
        self.token = HuShi.Config.params_config.token
        self.headers = HuShi.Config.params_config.headers

    def setUp(self):

        print("***************** Begin *******************")

    def test_Search_Meeting_Normal(self):
        params_dict = {"searchKey":"joke","pageNo":1,"pageSize":20}

        params = Parameter().Package_params(str(params_dict),self.token,self.signature)
        url = Environment().Test() + self.api
        try:
            result = requests.post(url,params,headers =  self.headers)
            Logging().Info("Request:"+ url + "  Parameters:"+ str(params))
            self.assertEqual(result.json()["code"],str(1),"断言错误，状态码错啦！！")
        except Exception as error:
            error_info = "<AssertionError> " + str(result.json()["code"]) + "≠ 1, Response:" + str(result.json())
            Logging().Error(error_info)
            raise error


    def test_Search_Meeting_NoContent(self):
        params_dict = {"searchKey":"","pageNo":1,"pageSize":20}
        params = Parameter().Package_params(str(params_dict), signature=self.signature)
        url = Environment().Test() + self.api
        try:
            result = requests.post(url,params,headers = self.headers)
            Logging().Info("Request:"+ url + "  Parameters:"+ str(params))
            self.assertEqual(result.json()["code"],2000022,"断言错误:状态码错啦！")

        except Exception as error:
            error_info = "<AssertionError> " + str(result.json()["code"]) + "≠ 2000021, Response:" + str(result.json())
            Logging().Error(error_info)
            raise error

    def tearDown(self):

        print("***************** End *******************")

if __name__ == "__main__":

    unittest.main()
    # # test_SearchMeeting().test_Search_Meeting_Normal()
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    #
    # # suite.addTest(test_SearchMeeting("test_Search_Meeting_NoContent"))
    # suite.addTest(loader.loadTestsFromTestCase(test_SearchMeeting))
    # print(suite)




# class test_Search_Meeting:
#
#     def __init__(self):
#
#         self.api = "/meeting/search"
#         self.signature = HuShi.Config.params_config.signature
#         self.token = HuShi.Config.params_config.token
#         self.headers = HuShi.Config.params_config.headers
#
#
#     def test_Search_Meeting_Normal(self):
#         params_dict = {"searchKey":"joke","pageNo":1,"pageSize":20}
#
#         params = Parameter().Package_params(str(params_dict),self.token,self.signature)
#         url = Environment().Test() + self.api
#         try:
#             result = requests.post(url,params,headers = self.headers)
#             Logging().Info("Request:"+ url + "  Parameters:"+ str(params))
#             assert result.json()["code"] == "1"
#         except Exception as error:
#             error_info = "<AssertionError> " + str(result.json()["code"]) + "≠ 1, Response:" + str(result.json())
#             Logging().Error(error_info)
#             raise error
#
#
#     def test_Search_Meeting_NoContent(self):
#         params_dict = {"searchKey":"","pageNo":1,"pageSize":20}
#         params = Parameter().Package_params(str(params_dict), signature=self.signature)
#         url = Environment().Test() + self.api
#         try:
#             result = requests.post(url,params,headers = self.headers)
#             Logging().Info("Request:"+ url + "  Parameters:"+ str(params))
#             assert result.json()["code"] == "2000021"
#         except Exception as error:
#             error_info = "<AssertionError> " + str(result.json()["code"]) + "≠ 2000021, Response:" + str(result.json())
#             Logging().Error(error_info)
#             raise error


