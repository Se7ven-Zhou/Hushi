# coding:utf-8

import requests
import sys
sys.path.append("C:/Users/Administrator/PycharmProjects/pythonStudy/venv")
from HuShi.Common.readData import Read_Data
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.TestCases.test_requests import Requests
import HuShi.Config.params_config
import pytest
import os
import time

if __name__ == "__main__":
    Requests().test_Requests("test_data.xlsx")