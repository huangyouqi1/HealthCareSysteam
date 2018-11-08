#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:python
@file: HealthCareSystem.py
@time: 2018/10/30
"""
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import main
if __name__ == '__main__':
    main.run()