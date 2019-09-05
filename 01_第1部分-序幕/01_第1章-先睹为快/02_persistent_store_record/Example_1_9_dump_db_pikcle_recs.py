#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 通过glob模块，为了得到一条记录，只需要载入一个记录文件而不是整个数据库

import pickle
from glob import glob

for filename in glob('*.pkl'):      # 针对 bob、sue、tom
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])     # 获取sue的名字
