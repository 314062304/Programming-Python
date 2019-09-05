#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 把基于类的记录持久化

import shelve
from Example_1_15_person import Person
from Example_1_16_manager import Manager


bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()