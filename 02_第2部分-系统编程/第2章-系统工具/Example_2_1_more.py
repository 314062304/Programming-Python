#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 自定义分页脚本

"""
分割字符串或文本文件并交互地进行分页
"""

def more(text, numlines=15):
    lines = text.splitlines()           # 效果类似split('\n'),不过不用在末尾加''
    while lines:
        chunk = lines[:numlines]        # lines[:15]是一个切片表达式,它获取列表中的头15项
        lines = lines[numlines:]        # lines[15:]则获取余下各项
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys                          # 运行时进行此操作,导入时不进行
    more(open(sys.argv[1]).read(), 10)  # 显示命令行里的文件的页面内容,向more函数的numlines参数传入10