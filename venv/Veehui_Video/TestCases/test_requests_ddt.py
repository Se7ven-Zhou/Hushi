# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.readData_DDT import Read_Data_ddt
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.Common.writeReport import WriteReport
import HuShi.Config.params_config
import unittest
import os
import time
import ddt

data_ddt = Read_Data_ddt("test_data_ddt.xlsx").Get_Data()


@ddt.ddt
class Requests(unittest.TestCase):

    def __init__(self,method):
        super(Requests, self).__init__(method)

        self.signature = HuShi.Config.params_config.signature
        self.token = HuShi.Config.params_config.token
        self.headers = HuShi.Config.params_config.headers

    @ddt.data(*data_ddt)
    def test_Requests(self,data):

        WriteReport().Creat_Report()
        params = Parameter().Package_params(data["params"], signature=self.signature)
        url = Environment().Test() + data["api"]

        try:
            # 请求
            result = requests.request(data["method"],url,params=params,headers=self.headers)
            Logging().Info("< Request:" + url + " >< Parameters:" + str(params) +" >< Respose: "+ str(result.json()))
            # 获取报告行数
            n = WriteReport().Get_MaxRow()

            assert int(result.json()["code"]) == data["code"], WriteReport().Write_Report(n+1,data["name"], data["api"], data["params"], data["code"],str(result.json()))
        except Exception as error:
            error_info = "<AssertionError> " + str(result.json()["code"]) + "≠" + str(data["code"]) + " <Response:" + str(result.json()) + ">"
            Logging().Error(error_info)
            raise error

if __name__ == "__main__":

    unittest.main()