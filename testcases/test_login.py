# -*- coding: utf-8 -*-
import unittest
from common import constant
from common.readExcel import ReadExcel
from common.logger import MyLog
from common.request import HttpRequest
from common.basic_data import Context
from common.basic_data import DoRegex
from common.config import ConfigLoader
from ddt import ddt,data
import json
import os


excel_path = os.path.join(constant.excel_path,"test_data.xlsx")
do_excel = ReadExcel(excel_path)
cases = do_excel.get_cases("Login")
@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    @data(*cases)
    def testLogin(self,case):
        data = case.data
        url_pre = ConfigLoader().get("api","url_pre")
        url = url_pre + case.url
        data = DoRegex().replace(data)
        MyLog.info("测试标题是：{0}".format(case.title))
        MyLog.info("测试数据是：{0}".format(data))
        data = json.loads(data)
        resp = HttpRequest(datas=data,url=url,method=case.method)
        try:
            resp.get_json()["error"]
        except:
            MyLog.info("测试通过")
        else:
            try:
                self.assertEqual(case.excepted, resp.get_json()["error"])
                MyLog.info("测试通过")
            except AssertionError as e:
                MyLog.error(e)
                raise e


    def tearDown(self):
        pass

