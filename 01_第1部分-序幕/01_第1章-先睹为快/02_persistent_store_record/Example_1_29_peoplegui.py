#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

"""
实现一个图形界面，用于查看和更新存储于shelve中的类实例，
该shelve保存在脚本运行的机器上，可能是一个或多个本地文件
"""

from tkinter import *
from tkinter.messagebox import showinfo
import shelve
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('Pelpel Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text="Fetch",  command=fetchRecord).pack(side=LEFT)      # 定义按键，按键位置top, bottom, left, or right
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)     # 定义按键，按键位置top, bottom, left, or right
    Button(window, text="Quit",   command=window.quit).pack(side=RIGHT)     # 定义按键，按键位置top, bottom, left, or right
    return window

def fetchRecord():
    key = entries['key'].get()      # 使用键获取数据，并在GUI中展示
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]        # 更新已有记录
    else:
        from Example_1_15_person import Person      # 在该键值下生成/保存新纪录
        record = Person(name='?', age='?')          # eval：字符串必须用引号括起来
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()