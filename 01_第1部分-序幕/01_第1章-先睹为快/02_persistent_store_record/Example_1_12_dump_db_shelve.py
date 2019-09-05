#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 重新打开shelve并通过键来取得它存储的记录

import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()