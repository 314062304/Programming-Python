#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys                      # 或者用sorted(sys.stdin)排序方法

lines = sys.stdin.readlines()   # 对输入的行数据进行排序
lines.sort()                    # 发送排序结果到stdout
for line in lines:              # 进一步处理
    print(line, end='')