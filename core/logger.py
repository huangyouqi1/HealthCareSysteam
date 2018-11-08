#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:python
@file: logger.py
@time: 2018/11/02
"""
import logging
from conf import settings
def logger(log_type):
    '''调试输出信息到终端和文件'''
    # 创建一个调试器
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 创建一个调试输出到终端的句柄
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # 创建一个调试输出到文件的句柄
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # 创建调试信息格式
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    # 添加格式到ch fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 添加ch fh 到 logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
