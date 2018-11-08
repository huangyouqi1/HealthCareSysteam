#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:python
@file: excel_module.py
@time: 2018/11/01
"""
import xlwt
import xlrd
import xlutils.copy
import functools
import os
from conf import  settings

account_file = "account_info.xls"
account_path = settings.BASE_DIR + os.sep + "db" + os.sep + account_file
#装饰器,确保每次检查本地数据的时候,文件是存在的 ,否则会报错
def creat_file(text):
    def decorator(func):
        # 保持函数原有的属性
        @functools.wraps(func)
        def wapper(*argc, **argv):
            # 先判断文件是否存在，否则创建文件
            if os.path.exists(account_path) is False:
                workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
                sheet = workbook.add_sheet('account', cell_overwrite_ok=True)
                sheet.write(0, 0, 'account')
                sheet.write(0, 1, 'password')
                sheet.write(0, 2, 'password_sh256')
                workbook.save(account_path)
            print('%s:%s'%(text, func.__name__))
            return func(*argc, **argv)
        return wapper
    return decorator

@creat_file("保存用户信息到本地excel")
def account_save(account):
    # 打开文件之后用xlutils.copy才能追加到表格
    data = xlrd.open_workbook(account_path)
    ws = xlutils.copy.copy(data)
    sheet = ws.get_sheet(0)
    # 获取现有行数追加数据并保持
    nrows = data.sheet_by_index(0).nrows
    sheet.write(nrows, 0, account["account"])
    sheet.write(nrows, 1, account["password"])
    sheet.write(nrows, 2, account["password_sh256"])
    ws.save(account_path)

@creat_file("检查用户名是否已注册过")
def account_isexit(account_num):
    book = xlrd.open_workbook(account_path)
    sheet = book.sheet_by_index(0)
    # 第一列是手机号码,遍历看是否以注册过
    account_list = sheet.col_values(0)
    for account in account_list:
        if account_num == account:
            return False
    return True

@creat_file("校验登录的用户名和密码")
def account_check(account_num,password):
    book = xlrd.open_workbook(account_path)
    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    for i in range(rows):
        accout_l = sheet.row_values(i)
        if accout_l[0] == account_num and accout_l[2] == password:
            return True
    return False

# import xlwt
# book = xlwt.Workbook(encoding='utf-8',style_compression=0)
# sheet = book.add_sheet('test',cell_overwrite_ok=True)
# sheet.write(0,0,'EnglishName')
# for i in range(1,10):
#     sheet.write(i,0,'Alex{}'.format(i))
# txt1 = '中文名字'
# sheet.write(0,1,txt1.decode('utf-8'))
# txt2 = '黄油漆'
# for i in range(1,10):
#     sheet.write(i,1,txt2.decode('utf-8')+'{}'.format(i))
# book.save(r'test.xls')

# import xlrd
# xlsfile = r'product_list.xls'
# book = xlrd.open_workbook(xlsfile)
# # 通过所以选择表
# sheet0 = book.sheet_by_index(0)
# sheet1 = book.sheet_by_index(1)
# sheet2 = book.sheet_by_index(2)
# # print (sheet0.name)
# # print (sheet1.name)
# # print (sheet2.name)
# # 表的名字
# # print (book.sheet_names())
# # sheet_name = sheet0.name
# sheet_name = book.sheet_names()[0]
# nrows = sheet0.nrows
# print (nrows)
# for i in range(nrows):
#     print (sheet0.row_values(i))
# # 读取一行数据
# print (sheet0.row_values(2))
# # 读取一列数据
# print (sheet0.col_values(1))
# # 通过坐标读取数据
# print (sheet0.cell_value(1,1))
