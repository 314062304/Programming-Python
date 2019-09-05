#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 因为MyGui被编写为类，GUI可以采用继承进行定制

from tkinter import *
from tkinter.messagebox import showinfo
from Example_1_25_tKinter102 import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()