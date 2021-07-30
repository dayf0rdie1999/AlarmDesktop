# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:14:52 2020

@author: Duong Anh Vu
"""

import datetime
import time




def main():
    print('haha')
    
    Timer1 = Timer(hour = 1, minute = 3, second = 0)
    
    

    

class Timer():
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.second = second
        self.minute = minute
        self.setTimeWatch();
        
    
    def setTimeWatch(self):
        self.timeWatch = datetime.time(self.hour,self.minute,self.second)
        self.strTimeWatch = self.timeWatch.strftime("%H:%M:%S")
      
    def checkTimeWatch(self,hour = 0, minute = 0, second = 0):
        self.timeWatch = datetime.time(hour,minute,second)
        self.strTimeWatch = self.timeWatch.strftime("%H:%M:%S")
        
#        self.TimeStart = True
#        while self.TimeStart == True
#        if self.second == 0:
#            self.second = 59
#            self.minute -= 1
#            
#        if self.minute == 0 and self.hour != 0:
#            self.hour -= 1
#            self.minute = 59
#            
#        self.second -= 1
#        self.timeWatch = datetime.time(self.hour,self.minute,self.second)
#        self.strTimeWatch = self.timeWatch.strftime("%H:%M:%S")
        
    def getTimeWatch(self):
        return self.timeWatch
    
    def getStrTimeWatch(self):
        return self.strTimeWatch



if __name__ == "__main__": main()