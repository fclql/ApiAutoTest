# -*- coding: utf-8 -*-
import unittest
from testcases import test_dress_list
from common import constant
import HtmlTestRunnerNew
from common.logger import MyLog


suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(test_dress_list.TestDressList))
try:
    with open(constant.report_path,mode="wb+") as file:
        runner = HtmlTestRunnerNew.HTMLTestRunner(stream=file,title="api_auto_test report")
        runner.run(suite)
except FileExistsError as e:
    MyLog.error(e)
    raise e

