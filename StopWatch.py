# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:55:14 2020

@author: Duong Anh Vu
"""

import datetime
import time
from time import perf_counter
from threading import Timer
import time




def main():
    print('haha')
    zeroTime1 = StopWatch()

    
    

    

class StopWatch():
    
    def __init__(self):
        self.hour = 0
        self.second = 0
        self.minute = 0
        self.milisecond = 0
        self.TimeStart = True
    
    def startTime(self):
        self.timeWatch = datetime.time(hour = self.hour,minute = self.minute,second = self.second,microsecond = self.milisecond)
        self.strTimeWatch = self.timeWatch.strftime("%H:%M:%S.%f")
#        self.hour = 0
#        self.second = 0
#        self.minute = 0
#        self.numberSecond = 0
#        self.milisecond = 0
#        self.TimeStart = True
#        while self.TimeStart == True:
#            time.sleep(0.001)
#            self.milisecond += 1000
#            self.timeWatch = datetime.time(hour = self.hour,minute = self.minute,second = self.second,microsecond = self.milisecond)
#            
#            if self.milisecond == 999000:
#                self.milisecond = 0;
#                self.second += 1;
#                
#            if self.second == 59:
#                self.second = 0
#                self.minute += 1
#                
#            if self.minute == 59:
#                self.hour += 1
#                self.minute = 0
#            
#            self.strtimeWatch = self.timeWatch.strftime("%H:%M:%S.%f")
#            print(self.strtimeWatch)
        
    def getStrTimeWatch(self):
        return self.strTimeWatch[:-4]
                
        
    def pauseStopWatch(self):
        self.TimeStart = False
                
    
    def resetTime(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.milisecond = 0
        self.startTime()
        self.TimeStart = False
    
    
if __name__ == "__main__": main()