# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:24:57 2020

@author: Duong Anh Vu
"""

from datetime import datetime
from datetime import time
from time import sleep
from CalendarDisplay import DateList
import MusicList

def main():
    checkList = []
    for i in range(7):
        checkList.append(False)
    
    checkList[2] = True
#    checkList[4] = True
    checkList[6] = True
    MusicalList = MusicList.musicList()
    Alarm1 = Alarm(22,10,"TestAlarm",checkList = checkList,song = MusicalList.fileList[1])
    print(Alarm1.getAlarm())
    print(Alarm1.checkRepeatDate())


    

    checkList_2 = []
    for e in range(7):
        checkList_2.append(False)
        
    checkList_2[2] = False
    checkList_2[6] = False
    checkList_2[3] = False
    checkList_2[5] = False
    Alarm1.editAlarm(21,10,"Test Alarm 2", checkList_2,MusicalList.fileList[2])
    print(Alarm1.Date)
    print(Alarm1.getAlarm())
    print(Alarm1.checkRepeatDate())
#    Alarm2 = Alarm(13,15,"Test Alarm2", checkList = checkList_2, song = MusicalList.fileList[2])
#    
#    print(Alarm2.checkRepeatDate())
#    print(Alarm1.checkRepeatDate())
#    Alarm2 = Alarm(13,1,"TestAlarm2",song =MusicalList.fileList[1])
#    print(Alarm2.getAlarm())
#    AlarmList1 = AlarmList()
#    AlarmList1.addAlarm(Alarm1)
#    AlarmList1.addAlarm(Alarm2)

#    AlarmOn(AlarmList1,MusicalList)
#    Alarm3 = Alarm(20,41,"TestAlarm2","Monday",song =MusicalList.fileList[1])
##    Alarm3 = Alarm(16,19,"MA345")
##    Alarm4 = Alarm(16,19,"AE313")
#    AlarmList1.addAlarm(Alarm2)
##    AlarmList1.addAlarm(Alarm3)
##    AlarmList1.addAlarm(Alarm4)
#    print(AlarmList1)
#    testAlarm = True
#    while testAlarm == True:
#        for _ in range(AlarmList1.getAlarmNumber()):
#            AlarmOn(AlarmList1, MusicalList)
#            
#        
#        testAlarm = AlarmList1.checkAlarmListStatus()
    
    
    
      	
#----------
# Creating a function to do sth when the alarm match the current time
def AlarmOn(alarmObjectList, MusicalList):
    
    alarmObjectList.startChecking();
    #Checking the
    AlarmListStatus = True;
    while AlarmListStatus == True:
        for alarmObject in alarmObjectList.alarmList:
            if alarmObject.getAlarmStatus() == True:
                now = datetime.now()
                nowMonth = datetime.now().month
                nowDay = datetime.now().day
                now = now.strftime("%H:%M:%S")
                repeatStatus = alarmObject.checkRepeatStatus()
                if str(now) == str(alarmObject.getAlarmTime()) and nowMonth == alarmObject.getMonth() and nowDay == alarmObject.getDay():
                    if repeatStatus == False and alarmObject.checkSnooze() == False:
                        alarmObject.setAlarmOff()
                        
                
                    alarmObject.play_sound()
                else:
                    pass
            elif alarmObject.getAlarmStatus() == False:
                pass
        AlarmListStatus  = alarmObjectList.checkAlarmListStatus();
    # When All the Alarm is turned off
    alarmObjectList.stopChecking();
    print("2 Stop Running")
    return AlarmListStatus;
        
    
    
    
#-----------
#Creating an alarm List
class AlarmList():
    
    def __init__(self):
        self.editAlarmSetting = False;
        self.addAlarmSetting = False;
        self.checkingStatus = False;
        self.alarmList = []
        self.alarmNumber = 0
        
    def setaddAlarmSettingOn(self):
        self.addAlarmSetting = True;
        
    def setaddAlarmSettingOff(self):
        self.addAlarmSetting = False;
        
    def getaddAlarmSettingOn(self):
        return self.addAlarmSetting;
    
    def setEditAlarmSettingOn(self):
        self.editAlarmSetting = True
        
    def setEditAlarmSettingOff(self):
        self.editAlarmSetting = False
        
    def getEditAlarmSetting(self):
        return self.editAlarmSetting
    
    def addAlarm(self,alarmObject):
        self.alarmList.append(alarmObject)
        self.alarmNumber += 1
        self.sortAlarmList()
        
    def deleteAlarm(self,alarmObject):
        self.alarmList.remove(alarmObject)
        self.alarmNumber -= 1
        self.sortAlarmList()
    
    def deleteAlarmIndex(self,index):
        del self.alarmList[index]
        self.alarmNumber -= 1
        self.sortAlarmList()
    
    def getAlarmNumber(self):
        return self.alarmNumber
    
    def checkAlarmList(self):
        for alarmObjectFirst in self.alarmList:
            indexFirst = self.alarmList.index(alarmObjectFirst);
            for alarmObjectRest in self.alarmList:
                indexRest = self.alarmList.index(alarmObjectRest);
                if alarmObjectFirst.getMonth() == alarmObjectRest.getMonth() and alarmObjectFirst.getDay() == alarmObjectRest.getDay() and str(alarmObjectFirst.getAlarmTime()) == str(alarmObjectRest.getAlarmTime()) and indexFirst != indexRest:                
                    self.deleteAlarm(alarmObjectRest)
                else:
                    pass

    def checkAlarmListStatus(self):
        self.numOn = 0
        self.numOff = 0
        for index in range(self.alarmNumber):
            if self.alarmList[index].getAlarmStatus() is True:
                self.numOn += 1
                
            elif self.alarmList[index].getAlarmStatus() is False:
                self.numOff += 1
                       
        if self.numOff == self.alarmNumber:
            return False
        else:
            return True
    
    def startChecking(self):
        self.checkingStatus = True;
    
    def stopChecking(self):
        self.checkingStatus = False;
        
    def sortAlarmList(self):
        pass
        

#-----------
# Creating an Alarm class
class Alarm():
    
    #Creating a constructor
    def __init__(self, hour = 0, minute = 0,title = "None",checkList = None, song = None, snooze = False, snoozeValue = 0):
        self.editMode = False
        self.checkList = checkList
        self.Date = []
        self.dayList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.snoozeValue = snoozeValue;
        self.snooze = snooze;
        self.MusicalList = MusicList.musicList();
        self.music_running = False;
        self.song = song
        self.nowMonth = datetime.now().month
        self.nowDay = datetime.now().day
        self.nowHour = datetime.now().hour
        self.nowMinute = datetime.now().minute
        self.dateList = None
        self.setAlarm(hour, minute, title)
        self.repeatDate(checkList)
        self.createAlarm()
        self.convertMonthAndDay()
        self.checkAlarm()

    
    # Setting an alarm
    def setAlarm(self, hour = 0, minute = 0, title = "None"):
        self.alarmStat = True
        self.title = title
        self.hour = hour
        self.fixedHour = hour
        self.minute = minute
        self.fixedMinute = minute
        self.AlarmTime = time(self.hour,self.minute)
    
    # Playing the music
    def play_sound(self):
        self.music_running = True
        self.MusicalList.playSong(self.song)
            
    
    def stop_sound(self):
        self.music_running = False
        self.MusicalList.stopPlay()
        
    def getMusicStatus(self):
        return self.music_running;
    
    
    #-----
    # Converting the string to int for proper comparison
    def convertMonthAndDay(self):
        self.dateTime, Trash = self.Alarm.split(' ')
        self.month,self.day = self.dateTime.split('/')
        self.month = int(self.month)
        self.day = int(self.day)
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
   
    
    def setSnoozeOn(self):
        self.snooze = True;
        
    def setSnoozeOff(self):
        self.snooze = False;
    
    def checkSnooze(self):
        return self.snooze;
    
    def snoozeMethod(self):
        sumTime = self.minute + self.snoozeValue
        if self.snoozeValue != 0 and sumTime < 60:
#            print("Through condition")
            self.editAlarm(self.hour, sumTime,self.title,self.checkList,self.song,self.snooze,self.snoozeValue)
        elif self.snoozeValue != 0 and sumTime > 60:
            self.editAlarm(self.hour + 1, sumTime - 60,self.title,self.checkList,self.song,self.snooze,self.snoozeValue)
        elif self.snoozeValue != 0 and sumTime > 60 and self.nowHour > 23:
            self.editAlarmDate(newDay = self.day + 1)
            self.editAlarm( self.hour + 1,  sumTime - 60,self.title,self.checkList,self.song,self.snooze,self.snoozeValue)
        # There will be an error if that person intentionally creating the alarm on the last day of the month at the last hour of the day)
        
    #----
    # Creating datelist
    def repeatDate(self, checkList = None):
        self.Date = []
        if checkList == None:
            pass
        if checkList != None:
            for index in range(len(self.dayList)):
                if checkList[index] == True:
                    self.dateList = DateList(self.dayList[index]);
                    self.Date += self.dateList.dateList;
                    self.Date.sort(key=lambda date: datetime.strptime(date, "%m/%d"))
                else:
                    pass
            if len(self.Date) != 0:
                self.firstMonth, self.firstDay = self.Date[0].split('/')
#                print(self.firstMonth)
#                print(self.firstDay)
#                print(self.nowDay)
#                print(self.nowMonth)
                if self.nowHour > self.hour and int(self.firstDay) != self.nowDay and int(self.firstMonth) != self.nowMonth:
#                    print("Haha")
                    self.today = str(self.nowMonth) + "/" + str(self.nowDay + 1);
                    self.Date.append(self.today)
                    pass
                elif self.nowHour > self.hour and self.nowMinute > self.minute and int(self.firstDay) != self.nowDay and int(self.firstMonth) != self.nowMonth:
#                    print("Haha 1")
                    self.today = str(self.nowMonth) + "/" + str(self.nowDay + 1);
                    self.Date.append(self.today);
                elif int(self.firstDay) != int(self.nowDay) and int(self.firstMonth) == int(self.nowMonth):
#                    print("Haha 2")
                    self.today = str(self.nowMonth) + "/" + str(self.nowDay);
                    self.Date.append(self.today)
                elif int(self.firstDay) != int(self.nowDay) and int(self.firstMonth) != int(self.nowMonth):
#                    print("Haha 3")
                    self.today = str(self.nowMonth) + "/" + str(self.nowDay);
                    self.Date.append(self.today)
                elif int(self.firstDay) == self.nowDay and int(self.firstMonth) == self.nowMonth:
                    pass
                self.Date.sort(key=lambda date: datetime.strptime(date, "%m/%d"))

            
    #--- Checking what day they are going to repeat
    def checkRepeatDate(self):
        if self.checkList != None:
            self.str = "Repeat ";
            for index in range(len(self.dayList)):
                if self.checkList[index] == True:
                    self.str += self.dayList[index] + "|";
            
            if self.checkList[0] == self.checkList[1] == self.checkList[2] == self.checkList[3] == self.checkList[4] == self.checkList[5] == self.checkList[6] == True:
                self.str = "Repeat EveryDay"
            
            elif self.checkList[0] == self.checkList[1] == self.checkList[2] == self.checkList[3] == self.checkList[4]  == True and self.checkList[5] == self.checkList[6] == False:
                self.str = "Repeat WeekDay"
            elif self.checkList[0] == self.checkList[1] == self.checkList[2] == self.checkList[4] == self.checkList[5] == self.checkList[6] == False:
                self.str = "None"
                pass
        elif self.checkList == None:
            self.str = "None"
        
        return self.str
    
    def createAlarm(self):
        if len(self.Date) > 1:
#            print(self.Date)
            self.Alarm = self.Date[0] + " " + str(self.AlarmTime)
        else:
            if self.nowHour > self.hour:
                self.Alarm = str(self.nowMonth) + "/" + str(self.nowDay + 1) + " " + str(self.AlarmTime)
            elif self.nowHour == self.hour and self.nowMinute > self.minute:
                self.Alarm = str(self.nowMonth) + "/" + str(self.nowDay + 1) + " " + str(self.AlarmTime)           
            else:
               self.Alarm = str(self.nowMonth) + "/" + str(self.nowDay) + " " + str(self.AlarmTime)
                
        
    def checkAlarm(self):
        self.convertMonthAndDay()
        self.nowMonth = datetime.now().month
        self.nowDay = datetime.now().day
        self.nowHour = datetime.now().hour
        self.nowMinute = datetime.now().minute
        if self.nowHour > self.hour and  self.nowMonth == self.month  and self.nowDay == self.day and len(self.Date) > 1:
            self.Alarm = self.Date[1] + " " + str(self.AlarmTime)
#            print(self.Alarm)
        elif self.nowHour == self.hour and self.nowMinute > self.minute and  self.nowMonth == self.month  and self.nowDay == self.day and len(self.Date) > 1 :
            self.Alarm = self.Date[1] + " " + str(self.AlarmTime)
#            print(self.Alarm)
            
        elif self.nowHour == self.hour and self.nowMinute > self.minute and  self.nowMonth == self.month  and self.nowDay == self.day:
            self.Alarm = str(self.nowMonth) + "/" + str(self.nowDay + 1) + " " + str(self.AlarmTime)
#            print(self.Alarm)
            
        elif self.nowHour == self.hour and self.nowMinute > self.minute and  self.nowMonth == self.month  and self.nowDay == self.day:
            self.Alarm = str(self.nowMonth) + "/" + str(self.nowDay + 1) + " " + str(self.AlarmTime)
#            print(self.Alarm)
        
    def addrepeatDate(self):
        pass
    
    def getAlarmTime(self):
        return self.AlarmTime
    
    def getHour(self):
        return self.hour
    
    def getMinute(self):
        return self.minute
    
    #Getting all the information of the Alarm
    def getAlarm(self):
        return self.Alarm
    
    # Getting the Title of the Alarm
    def getTitle(self):
    	return self.title
    # Setting the status of the Alarm
    def setAlarmOff(self):
    	self.alarmStat = False
    
    # Setting the status of the Alarm	
    def setAlarmOn(self):
        self.alarmStat = True
    
    # Getting the alarm status
    def getAlarmStatus(self):
    	return self.alarmStat
    
    # Getting the repeat status of the alarm
    def checkRepeatStatus(self):
        if self.dateList == None:
            return False
        else:
            return True
    
    
    # Reseting the Alarm Time back to the beginning;
    def resetAlarmTime(self):
        self.editAlarm(self.fixedHour,self.fixedMinute,self.title, self.checkList, self.song,self.snooze,self.snoozeValue)
        
    #Get EditMode;
    def setEditModeOn(self):
        self.editMode = True;
        
    def setEditModeOff(self):
        self.editMode = False;
        
    def getEditMode(self):
        return self.editMode;
        
    # Edit The Alarm
    def editAlarm(self,newHour = 0, newMinute = 0,newTitle = "None", NewcheckList = None,newSong = None, snoozeMode = False, newSnoozeValue = 0):
        if newTitle != "None":
            self.title = newTitle
        
        if self.hour != newHour and self.editMode == True:
            self.hour = newHour
            self.fixedHour = self.hour
            
        else:
            self.hour = newHour
        
        if self.minute != newMinute and self.editMode == True:
            self.minute = newMinute
            self.fixedMinute = self.minute
            
        else:
            self.minute = newMinute
        
        if NewcheckList != self.checkList:
            self.checkList = NewcheckList
            self.repeatDate(NewcheckList)
            
        if newSong != self.song:
            self.song = newSong
            
        if snoozeMode == True:
            self.snooze = snoozeMode
            self.snoozeValue = newSnoozeValue
            
        elif snoozeMode == False:
            self.snooze = snoozeMode;
            self.snoozeValue = 0;
            
        self.AlarmTime = time(self.hour,self.minute)
        self.editAlarmDate()
        
    def editAlarmDate(self,newDay = 0, newMonth = 0):
         
        if newDay != 0:
            self.day = newDay
            
        if newMonth != 0:
            self.month = newMonth
        
        if len(self.Date) != 0:
            self.Alarm = self.Date[0] + " " + str(self.AlarmTime)
            
        else:
            self.Alarm = str(self.month) + "/" + str(self.day) + " " + str(self.AlarmTime);
#        
#    def editAlarmRepeatedDate(self,checkList):
#        pass
    
if __name__ == "__main__": main()
