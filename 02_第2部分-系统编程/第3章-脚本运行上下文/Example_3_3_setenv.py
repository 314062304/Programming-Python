#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 修改shell变量
# 简单地修改shell变量USER，然后派生另一个脚本进程读取该变量值

import os
print('setenv...', end=' ')
print(os.environ['USER'])           # 输出当前shell的变量值

os.environ['USER'] = 'Brian'        # 在后台运行 os.putenv
os.system('python Example_3_4_echoenv.py')

os.environ['USER'] = 'Arthur'       # 传递更新值到衍生程序
os.system('python Example_3_4_echoenv.py')      # 链接的C语言库模块

os.environ['USER'] = input('?')
print(os.popen('python Example_3_4_echoenv.py').read())

