# -*- coding: utf-8 -*-
import unittest
from common.request import HttpRequest
from ddt import ddt,data
from common.readExcel import ReadExcel
from common.logger import MyLog
from common import constant
from common.basic_data import DoRegex,Context
from common.config import ConfigLoader
import os
import json


excel_file = os.path.join(constant.excel_path,"test_data.xlsx")
cases = ReadExcel(excel_file).get_cases("Search")

@ddt
class TestDressList(unittest.TestCase):
    def setUp(self):
        pass

    @data(*cases)
    def testDressList(self,case):
        data = case.data
        url = ConfigLoader().get("api","url_pre") + case.url
        data = DoRegex().replace(data)
        data = json.loads(data)
        resp = HttpRequest(url=url,method=case.method,datas=data)
        MyLog.info(resp.get_json())
        if resp.get_cookies():
            sessionid = resp.get_cookies()["tloa_login_sessionid"]
            setattr(Context,"sessionid",sessionid)
        else:
            pass
        try:
            resp.get_json()["error"]
        except:
            MyLog.info("测试通过")
        else:
            try:
                self.assertEqual(resp.get_json()["msg"],case.excepted)
            except AssertionError as e:
                MyLog.error(e)
                raise e

    def tearDown(self):
        pass
