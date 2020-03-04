# -*- coding: utf-8 -*-

'''
1.定义日志收集器
2.设定级别 debug info worning error critical
3.设置日志格式
4.指定输出渠道
5.收集日志
6.渠道关闭
'''
import os
import time
import logging
import HtmlTestRunnerNew
from common import constant


logger = logging.getLogger("fuchen")
logger.setLevel("DEBUG")

def set_handler(levels):
    if levels == "error":
        logger.addHandler(MyLog.error_handler)
    else:
        logger.addHandler(MyLog.handler)
        logger.addHandler(MyLog.report_handler)
    logger.addHandler(MyLog.ch)
    logger.addHandler(MyLog.report_handler)

def remove_handler(levels):
    if levels == "error":
        logger.removeHandler(MyLog.error_handler)
    else:
        logger.removeHandler(MyLog.handler)

def get_current_day(): #  获取当天
    return time.strftime('%Y%m%d',time.localtime(time.time()))

def get_log_dir():
    log_dir = os.path.join(constant.log_path,get_current_day())
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    return log_dir

class MyLog:
    log_dir = get_log_dir()
    log_file = os.path.join(log_dir,"logs.log")
    error_file = os.path.join(log_dir,"error.log")
    # 设置日志输出格式
    formatter = logging.Formatter("[%(asctime)s - %(name)s - %(levelname)s ]: %(message)s")
    # 指定输出渠道
    ## 指定控制台输出
    ch = logging.StreamHandler()
    ch.setLevel("DEBUG")
    ch.setFormatter(formatter)

    # info 文件输出
    handler = logging.FileHandler(filename=log_file, encoding='utf-8')
    handler.setLevel("INFO")
    handler.setFormatter(formatter)

    # error 文件输出
    error_handler = logging.FileHandler(filename=error_file, encoding='utf-8')
    error_handler.setLevel("ERROR")
    error_handler.setFormatter(formatter)

    # 报表日志输出
    report_handler = logging.StreamHandler(HtmlTestRunnerNew.stdout_redirector)
    report_handler.setLevel("INFO")
    report_handler.setFormatter(formatter)

    @staticmethod
    def debug(msg):
        set_handler("debug")
        logger.debug(msg)
        remove_handler("debug")

    @staticmethod
    def info(msg):
        set_handler("info")
        logger.info(msg)
        remove_handler("info")

    @staticmethod
    def error(msg):
        set_handler("error")
        logger.error(msg, exc_info=True)
        remove_handler("error")

