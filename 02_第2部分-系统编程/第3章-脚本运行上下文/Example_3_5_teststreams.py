#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 重定向流到文件或程序

"read numbers till eof and show squares"

def interact():
    print('Hello stream world!')  # 输出数据到 sys.stdout
    while True:
        try:
            reply = input('Enter a number>')     # 输入来自 sys.stdin的数据
        except EOFError:
            break                 # 在结尾抛出一个异常
        else:                     # 输出已有的字符串
            num = int(reply)
            print('%d squared is %d' % (num, num ** 2))
    print('Bye')

if __name__ == '__main__':
    interact()          # 在运行是不再导入数据

# Windows下文件结束符为Ctrl + z ，Unix下为Ctrl + d