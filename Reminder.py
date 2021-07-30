# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:47:27 2020

@author: Duong Anh Vu
"""

import datetime

def main():
    print("Haha")
    note1 = "This is the testing"
    reminder1 = Reminder(2020,1,7,12,5,note1)
    
    

class Reminder():
    
    def __init__(self,year = 2020,month = 1,day = 1,hour = 0,minute = 0,note = "haha"):
        self.createReminder(year,month,day,hour,minute,note)
        self.reminding()

    def reminding(self):
        self.today = datetime.datetime.today()
        self.today = self.today.strftime("%h/%d/%Y %H:%M")
        if self.today == self.reminderTime:
            print(self.reminderTime + ' ' + self.reminderNote)
    
    def createReminder(self, year, month, day, hour, minute, note ):    
        self.reminderTime = datetime.datetime(year,month,day,hour,minute)
        self.reminderTime = self.reminderTime.strftime("%h/%d/%Y %H:%M")
        self.reminderNote = note
        
        
    def getReminderTime(self):
        return self.reminderTime
        
    def getReminderNote(self):
        return self.reminderNote


if __name__ == "__main__": main()
