# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:59:59 2020

@author: Duong Anh Vu
"""

import calendar
import datetime

def main():
    
    Sunday = DateList("Wednesday")
#    print(Sunday.getDateList())
    
    Monday = DateList("Monday")
#    print(Monday.getDateList())
    
    SunAndMon = Monday.dateList + Sunday.dateList;
    SunAndMon.sort();
    print(SunAndMon)


    
    
class DateList():
    def __init__(self,dateName = "Monday"):
        self.getToday()
        self.dayList = []
        self.dateList = []
        self.dateNum = 0
        self.addDateList(dateName)
        self.updatedList()
        
        
    # adding all the monday date for entire year
    def addDateList(self,dateName = "Monday"):
        dateName = dateName.upper()
        
        self.month = [1,2,3,4,5,6,7,8,9,10,11,12]
        for month in range(1,len(self.month)+1):
            mycalendar = calendar.monthcalendar(2020, month)
            
            # Creating a list that is changing for each month
            weekList = []
            for week in range(0,5):
                weekList.append(mycalendar[week])
            
            
            if weekList[0][getattr(calendar,dateName)] != 0:
                self.dayList.append(weekList[0][getattr(calendar,dateName)])
                name = str(month) +  "/" + str(weekList[0][getattr(calendar,dateName)])
                self.dateList.append(name)
                self.dateNum += 1
                
                for i in range(1,4):
                    self.dayList.append(weekList[i][getattr(calendar,dateName)])
                    name = str(month) +  "/" + str(weekList[i][getattr(calendar,dateName)])
                    self.dateList.append(name)
                    self.dateNum += 1
                    
                self.updatedList()
    
            else:
                self.dayList.append(weekList[1][getattr(calendar,dateName)])
                name = str(month) +  "/" + str(weekList[1][getattr(calendar,dateName)])
                self.dateList.append(name)
                self.dateNum += 1
                
                for i in range(2,5):
                    self.dayList.append(weekList[i][getattr(calendar,dateName)])
                    name = str(month) +  "/" + str(weekList[i][getattr(calendar,dateName)])
                    self.dateList.append(name)
                    self.dateNum += 1
                    
                self.updatedList()
            
    
    # Removing holiday that has the same day on the calendar      
    def deleteDate(self):
        pass
           
    def getToday(self):
        self.year = datetime.datetime.now().year
        self.monthNow = datetime.datetime.now().month
        self.dayNow = datetime.datetime.now().day
        self.dateNow = str(self.monthNow) + "/" + str(self.dayNow)
    
    # Recreate the method, because the last method doesn't work out
    def updatedList(self):
        for index in self.dateList:
            month, day = index.split("/")
            month = int(month)
            day = int(day)
            monthNow = int(self.monthNow)
            dayNow = int(self.dayNow)
            
            if month < monthNow:
                self.dateList.remove(index)
                self.dateNum -= 1
                
            elif month == monthNow:
                if day < dayNow:
                    self.dateList.remove(index)
                    self.dateNum -= 1
                    
                    
    def printDateList(self):
        for k in range(len(self.dateList)):
            print(self.dateList[k])
            
    def getDateList(self):
        return self.dateList
    
    def getDateNum(self):
        return self.dateNum

    def getdayList(self):
        return self.dayList
    
    

if __name__ == "__main__": main()
