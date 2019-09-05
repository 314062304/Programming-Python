#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"collect command-line options in a dictionary"

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':           # 找到 '-名称 值' 键值对
            opts[argv[0]] = argv[1]     # 字典关键字为参数 '-名称'
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts

if __name__ == '__main__':
    from sys import argv                # 示例的客户端代码
    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)