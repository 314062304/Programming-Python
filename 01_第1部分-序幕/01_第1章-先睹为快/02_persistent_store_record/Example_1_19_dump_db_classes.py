#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 使用构建脚本创建shelve后调用shelve的转存脚本的输出

import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastname())
print(db['tom'].lastname())