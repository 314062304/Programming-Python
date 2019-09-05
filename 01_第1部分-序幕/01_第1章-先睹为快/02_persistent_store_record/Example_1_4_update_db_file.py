#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 实用脚本
""" 通过载入、更新和重新保存等操作对数据库进行了一些修改 """

from Example_1_2_make_db_file import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)