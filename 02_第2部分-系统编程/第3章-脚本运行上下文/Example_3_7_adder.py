#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sum = 0         # 定义全局变量
while True:
    try:
        line = input()      # 调用 sys.stdin.readlines()方法
    except EOFError:        # 用于 sys.stdin:中行的异常类型
        break               # 在结果输入 \n 换行符
    else:
        sum += int(line)    # 第二个ed处的sting.atoi() 方法
print(sum)