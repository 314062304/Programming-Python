#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import pickle

dbfile = open('people-pickle', 'rb')        # 使用3.x的二进制模式文件
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'


dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()