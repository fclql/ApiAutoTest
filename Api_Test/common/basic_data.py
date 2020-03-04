# -*- coding: utf-8 -*-
import re
import os
from common.readExcel import ReadExcel
from common import constant


class Context:
    from common.config import ConfigLoader
    config = ConfigLoader()
    user = config.get("basic","user")
    pwd = config.get("basic","pwd")

class DoRegex:
    def replace(self,target):
        pattern = "\$\{(.*?)\}"
        while re.search(pattern, target):
            key = re.search(pattern, target).group(1)
            try:
                key_value = getattr(Context, key)
            except Exception as e:
                print("请检查excel文件中的引用格式")
                raise e
            target = re.sub(pattern, key_value, target, count=1)
        return target
