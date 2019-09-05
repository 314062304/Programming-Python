#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 实用脚本
""" 每次运行时会重新将文件载入数据库 """

from Example_1_2_make_db_file import loadDbase

db = loadDbase()
for key in db:
    print(key, '=>\n  ', db[key])
print(db['sue']['name'])



