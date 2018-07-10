# coding:utf-8


import os
import time
import unittest
import Veehui_Video.Config.params_config
import HTMLTestRunnerNew
from Veehui_Video.Config.env_config import Environment
from Veehui_Video.Common.logger import Logging
from Veehui_Video.TestCases import test_searchMeeting
from Veehui_Video.TestCases.test_searchMeeting import test_SearchMeeting

if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径

    # suite.addTest(loader.loadTestsFromTestCase(test_SearchMeeting))
    suite.addTest(loader.loadTestsFromModule(test_searchMeeting))

    now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    report_address = os.getcwd() + "\Reports"
    report_name = "python_unittest_" + now + ".html"
    report_path = os.path.join(report_address,report_name)
    print(report_path)
    with open(report_path, "wb+") as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="Requests_AutoTest", tester="Seven")
        runner.run(suite)

