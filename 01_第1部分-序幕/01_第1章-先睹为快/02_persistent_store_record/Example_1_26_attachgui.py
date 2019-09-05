#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 将tKinter102创建的控件作为包添加在其他GUI内

from tkinter import *
from Example_1_25_tKinter102 import MyGui

# 应用主窗口
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# 弹出窗口
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()