#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 将内存中的字典对象存储到shelve中以永久保存

from initdata import bob, sue
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
