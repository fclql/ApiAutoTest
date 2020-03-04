# -*- coding: utf-8 -*-
import requests


class HttpRequest:

    def __init__(self, url, method, datas, json=None, cookies=None):
        if method == "get":
            self.resp = requests.get(url=url, params=datas,verify = False)
        elif json:
            self.resp = requests.post(url=url, json=json,cookies=cookies, verify = False)
        else:
            self.resp = requests.post(url=url, data=datas,cookies=cookies, verify = False)

    def get_status_code(self):
        return self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()

    def get_cookies(self):
        return self.resp.cookies
