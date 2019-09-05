#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')        # 使用3.x的二进制模式文件
pickle.dump(db, dbfile)                     # 字节数据，而非字符串
dbfile.close()