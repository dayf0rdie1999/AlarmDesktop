# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:10:30 2020

@author: Unknown
"""

from tkinter import *
import datetime

root = Tk()

lab = Label(root)


def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

# run first time
clock()

root.mainloop()