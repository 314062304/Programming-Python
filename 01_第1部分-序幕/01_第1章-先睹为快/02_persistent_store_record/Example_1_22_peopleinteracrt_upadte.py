#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 交互式的更新

import shelve

from Example_1_15_person import Person

fieldnames  = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key:
        break
    if key in db:
        record = db[key]        # 更新存在的记录
    else:                       # 或创建/保存新的记录
        record = Person(name='?', age='?')      # eval：引号字符串
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()