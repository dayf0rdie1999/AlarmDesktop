# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:02:11 2020

@author: Duong Anh Vu

Description: Designing the clock class with GUI
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
import time
import datetime

def main():
    clock1 = Timer()
    clock1.ObjectClock.win.mainloop()

class Clock(tk.Frame):
    
    def __init__(self):
        self.setWin()
        self.createtab1()
        self.setTime()
    
    def setTime(self):
        self.labelfont = ('times', 24)
        self.todayTime = time.strftime("Don't Waste Your Time: %H:%M:%S", time.localtime())
        self.label1 = ttk.Label(self.tab1Frame,text = self.todayTime, width = 30, font = self.labelfont).grid(column=1,row=0)
        self.win.after(1000,self.setTime)
        pass
 
        
    
    def setWin(self):
        self.win = tk.Tk()
        self.win.title("TimeApplication")
        
        
    def createtab1(self):
        
        #Creating a Tab control
        self.tabControl = ttk.Notebook(self.win)     # Create Tab Control

        self.tab1 = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.tab1, text='The Current Time') 
        

        self.tabControl.pack(expand=1, fill="both")
        
        self.tab1Frame = ttk.LabelFrame(self.tab1, text='The Clock')
        self.tab1Frame.grid(column=0, row=0, padx=8, pady=4)


class Timer():
    def __init__(self):
        self.ObjectClock = Clock()
        self.createTab2()
        self.setTimer()
        self.setHour()
        self.setMinutes()
        
    # Creating a timer
    def setTimer(self, **agrs):
        self.timeIn = datetime.time()
        self.label2 = ttk.Label(self.tab2Frame, text = self.timeIn, font = self.ObjectClock.labelfont).grid(column = 0, row = 0)
        
    # Creating a method to get and set hours
    def setHour(self, hour = 0):
        '''hourFont = ('times', 12)
        self.label3 = ttk.Label(self.tab2Frame, text = "Hour", font = hourFont).grid(column = 0, row = 1)
        self.hourSpin = Spinbox (self.tab2Frame, from_ = 0, to = 12, width = 5)
        self.hourSpin.grid(column = 0, row = 2, sticky = "W")'''
        pass
    
    def getHour(self):
        pass
    # Creating a method to get and set minutes
    def setMinutes(self,minutes = 0 ):
        #minutesFont = ('times', 12)
        #self.label3 = ttk.Label(self.tab2Frame, text = "Minutes", font = minutesFont, anchor= 'w').grid(column = 1, row = 1)
        #self.hourSpin = Spinbox (self.tab2Frame, from_ = 0, to = 60, width = 5)
        #self.hourSpin.grid(column = 1, row = 2, sticky = "W")
        pass
    def getMinutes(self,minutes):
        pass
    
    # Creating a tab to contain this method
    def createTab2(self):
        # Add A tab
        self.tab2 = ttk.Frame(self.ObjectClock.tabControl)
        self.ObjectClock.tabControl.add(self.tab2, text = 'The Timer')
        
        self.tab2Frame = ttk.LabelFrame(self.tab2, text='Timer')
        self.tab2Frame.grid(column=0, row=0,  padx=8, pady=4, sticky = "W")
        
        self.label1Frame = ttk.LabelFrame(self.tab2Frame, text = 'Settings')
        self.label1Frame.grid(column = 0 , row = 0, sticky = "W")
        
    
        
        
        
        
if __name__ == "__main__": main()