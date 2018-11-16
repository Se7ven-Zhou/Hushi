# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
import HuShi.Config.params_config
import pytest
import os
import time


@pytest.mark.smoke
def test_Search_Meeting_Normal():
    # 登录信息
    api = "/meeting/search"
    signature = HuShi.Config.params_config.signature
    token = HuShi.Config.params_config.token
    params_dict = {"searchKey": "笑话", "pageNo": 1, "pageSize": 20}
    headers = HuShi.Config.params_config.headers

    params = Parameter().Package_params(str(params_dict), token=token, signature=signature)
    url = Environment().Test() + api
    try:
        result = requests.post(url, params, headers=headers)
        assert result.json()["code"] == "1"
    except Exception as error:
        info = "AssertionError - " + str(result.json()) + "==> 1"
        Logging().Error(info)
        raise error

@pytest.mark.smoke
def test_Search_Meeting_NoContent():
    api = "/meeting/search"
    signature = HuShi.Config.params_config.signature
    params_dict = {"searchKey":"","pageNo":1,"pageSize":20}
    headers = HuShi.Config.params_config.headers

    params = Parameter().Package_params(str(params_dict),signature=signature)
    url = Environment().Test() + api
    try:
        result = requests.post(url,params,headers = headers)
        assert result.json()["code"] == "2000021"
    except Exception as error:
        info = "AssertionError - " + str(result.json()) + "==> 2000021"
        Logging().Error(info)
        raise error


if __name__ == "__main__":
    test_Search_Meeting_NoContent()
    # report_path = os.getcwd() + "\Reports" # 测试报告地址
    #
    # now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    # report_name = "Smoke_Test" + now + ".html"
    #
    # test_report_path = os.path.join(report_path,report_name)
    #
    # # print(test_report_path)
    #
    # pytest.main(["-m","smoke","--html",test_report_path])
