# coding:utf-8

import requests
from Veehui_Video.Common.readData import Read_Data
from Veehui_Video.Common.logger import Logging
from Veehui_Video.Common.package_params import Parameter
from Veehui_Video.Config.env_config import Environment
from Veehui_Video.TestCases.test_requests import Requests
import Veehui_Video.Config.params_config
import pytest
import os
import time

if __name__ == "__main__":
    Requests().test_Requests("test_data.xlsx")