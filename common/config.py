# -*- coding: utf-8 -*-
#配置文件的读取
import configparser
from common.constant import *
import os


class ConfigLoader:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        filename = os.path.join(conf_path,"global.conf")
        self.conf.read(filename)
        if self.conf.getboolean("switch","on"):
            filename = os.path.join(conf_path,"online.conf")
            self.conf.read(filename)
        else:
            filename = os.path.join(conf_path, "test.conf")
            self.conf.read(filename)

    def get(self,section,option):
        return self.conf.get(section=section, option=option)

    def getboolean(self,section,option):
        return self.conf.getboolean(section=section, option=option)

    def getint(self,section,option):
        return self.conf.getint(section=section,option=option)

    def getfloat(self,section,option):
        return self.conf.getfloat(section=section,option=option)

# if __name__ == '__main__':
#     config = configparser.ConfigParser()
#     file_path = os.path.join(excel_path,"global.conf")
#     config.read(file_path)
#     config.get(section="switch",option="on")