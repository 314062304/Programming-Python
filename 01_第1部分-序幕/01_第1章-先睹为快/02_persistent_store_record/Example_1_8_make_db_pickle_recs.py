#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 每条记录使用一个pickle文件
# 将每条记录存储到对应的普通文件中，已记录本身的键为文件名，以.pkl为后缀（在当前工作目录内创建了文件bob.pkl、 sue.pkl、 tom.pkl）

from initdata import bob, sue, tom
import pickle

for (key, record) in [('bob', bob), ('sue', sue), ('tom', tom)]:
     recfile = open(key + '.pkl', 'wb')
     pickle.dump(record, recfile)
     recfile.close()