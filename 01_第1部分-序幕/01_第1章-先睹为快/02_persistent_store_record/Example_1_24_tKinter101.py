#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 单击按钮时，程序会运行reply函数

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()