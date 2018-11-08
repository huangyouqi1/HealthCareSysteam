#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:python
@file: main.py
@time: 2018/10/31
"""
from core import PyQt5_Ui
# 存储用户数据的一个临时变量
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data' : None,
}
account_info = {
    "account": None,
    "password": None,
    "password_sh256": None,
}


def run():
    PyQt5_Ui.loginaccount()
