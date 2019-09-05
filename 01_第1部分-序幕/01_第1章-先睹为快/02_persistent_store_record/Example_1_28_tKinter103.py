#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')
# top.iconbitmap('py-blue-trans-out.ico')       # 调用脚本的图表失败，图表与平台的相关性可是臭名昭著的

Label(top, text='Enter your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()