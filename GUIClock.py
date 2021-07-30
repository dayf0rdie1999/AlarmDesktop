# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:31:12 2020

@author: Duong Anh Vu
"""


import tkinter as tk
import Alarm
import Reminder
import StopWatch
import Timer
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox


def main():
    print("haha")
    clock = GUIClock()
    clock.win.mainloop()
    
    
class GUIClock(tk.Frame):
    
    def __init__(self):
        self.setWin()
        self.Menubar()
        
    
    def setWin(self):
        self.win = tk.Tk()
        self.win.title("TimeApplication")
        self.win.geometry("1000x500")
        
    def quitGUI(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def Menubar(self):
        #Creating a menu bar
        self.menuBar = Menu(self.win)
        self.win.config(menu=self.menuBar)
        
        # Add menu items
        self.fileMenu = Menu(self.menuBar, tearoff = 0)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = "Quit", command = self.quitGUI)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        
        #Add Setting Menu
        self.settingsMenu = Menu(self.menuBar, tearoff = 0)
        self.settingsMenu.add_command(label = "Alarm", command = self.AlarmGUI)
        self.settingsMenu.add_separator()
        self.settingsMenu.add_command(label = "Stopwatch",command = self.StopWatchGUI)
        self.settingsMenu.add_separator()
        self.settingsMenu.add_command(label = "Timer")
        self.settingsMenu.add_separator()
        self.settingsMenu.add_command(label = "Reminder")
        self.menuBar.add_cascade(label="Settings", menu=self.settingsMenu)
        
        
    def AlarmGUI(self):
        
        self.AlarmGUIstyle = ttk.Style()
        self.AlarmGUIstyle.theme_create("TabStyle", parent = "alt", settings={
                "TNotebook": {"configure":{"tabmargins": [2,5,2,0]}},
                "TNotebook.Tab": {"configure": {"padding":[30,10]},}})
    
        self.AlarmGUIstyle.theme_use("TabStyle")
        
        
        # Creating the tabcontrol on my Notebook
        self.tabControl = ttk.Notebook(self.win)
        
        # Creating all the tabs
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text = 'Add')
        
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text = 'Edit')
        
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text = 'Delete')
        
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab4, text = 'Clone')
        
        self.tabControl.pack(expand = True, fill = "both")
        
    def StopWatchGUI(self):
        # Creating a style for the Stop Watch
        
        
        self.labelFrame1 = ttk.LabelFrame(self.win, text = "Stop-Watch")
        self.labelFrame1.grid(column = 0, row = 0, padx = 3, pady = 5 )
        
        self.Label1 = ttk.Label(self.labelFrame1, text = "haha").grid(column = 1, row = 0)
        


if __name__ == "__main__": main()
