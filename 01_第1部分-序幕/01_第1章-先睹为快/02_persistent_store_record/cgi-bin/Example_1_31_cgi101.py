#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import cgi

form = cgi.FieldStorage()               # 解析表单数据
print('Content-type: text/html\n')      # hdr加回车
print('<title>Reply Page</title>')      # html响应页面
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))