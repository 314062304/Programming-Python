#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 把GUI编写成tkinter的Frame控件的子类

from tkinter import *
from tkinter.messagebox import showinfo

class  MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()