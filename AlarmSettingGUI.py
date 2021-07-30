# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlarmSettingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Alarm import Alarm
from datetime import datetime
from Alarm import AlarmList
from Alarm import AlarmOn
import MusicList
from pathlib import Path
import threading
from threading import Timer
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
            base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_Form(QtCore.QObject):
#    finished = QtCore.pyqtSignal();
    
    def setupUi(self, Form):
        super(Ui_Form,self).__init__()
        Form.setObjectName("Form")
        Form.resize(412, 615)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setWindowIcon(QtGui.QIcon(resource_path("icon/Alarm.ico")))
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 47, 13))
        self.label_3.setObjectName("label_3")
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 203, 253))
        self.widget.setObjectName("widget")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #-----spinHour--------
        self.spinHour = QtWidgets.QSpinBox(self.groupBox)
        self.spinHour.setReadOnly(False)
        self.spinHour.setProperty("value", 24)
        self.spinHour.setObjectName("spinHour")
        #Setting spinHour range from 0 -> 24
        self.spinHour.setRange(0,23)
        self.horizontalLayout.addWidget(self.spinHour)
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        #-----spinMinute--------
        self.spinMinute = QtWidgets.QSpinBox(self.groupBox)
        self.spinMinute.setReadOnly(False)
        self.spinMinute.setObjectName("spinMinute")
        #Setting spinMinute range from 0 -> 60
        self.spinMinute.setRange(0,59)
        self.horizontalLayout.addWidget(self.spinMinute)
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        
        #--- Create Push Button ----
#        self.buttonTime = QtWidgets.QPushButton(self.widget)
#        self.buttonTime.setObjectName("buttonTime")
#        icon = QtGui.QIcon()
#        icon.addPixmap(QtGui.QPixmap("icon/alarm-636561.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#        self.buttonTime.setIcon(icon)
#        self.horizontalLayout.addWidget(self.buttonTime)
        
        #Connect the readSpinBox method
#        self.buttonTime.clicked.connect(self.readSpinBox)
        
        
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #-----MondayCheckBox--------
        self.checkBoxMon = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxMon.setObjectName("checkBoxMon")
        self.verticalLayout.addWidget(self.checkBoxMon)
        
        
        #-----TuesdayCheckBox--------
        self.checkBoxTues = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxTues.setObjectName("checkBoxTues")
        self.verticalLayout.addWidget(self.checkBoxTues)
        
        #-----WednesdayCheckBox--------
        self.checkBoxWed = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxWed.setObjectName("checkBoxWed")
        self.verticalLayout.addWidget(self.checkBoxWed)
        
        #-----ThursdayCheckBox--------
        self.checkBoxThurs = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxThurs.setObjectName("checkBoxThurs")
        self.verticalLayout.addWidget(self.checkBoxThurs)
        
        #-----FridayCheckBox--------
        self.checkBoxFri = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxFri.setObjectName("checkBoxFri")
        self.verticalLayout.addWidget(self.checkBoxFri)
        
        #-----SaturdayCheckBox--------
        self.checkBoxSat = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxSat.setObjectName("checkBoxSat")
        self.verticalLayout.addWidget(self.checkBoxSat)
        
        #-----SundayCheckBox--------
        self.checkBoxSun = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxSun.setObjectName("checkBoxSun")
        self.verticalLayout.addWidget(self.checkBoxSun)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        
        #----- Plain Text-------
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 300, 221, 101))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 440, 197, 111))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        
        
        
        #---- Vol Check Box-------
#        self.checkBoxVol = QtWidgets.QCheckBox(self.widget1)
#        self.checkBoxVol.setObjectName("checkBoxVol")
#        self.verticalLayout_3.addWidget(self.checkBoxVol)
        
        #---- Sound Check Box -----
#        self.checkBoxSound = QtWidgets.QCheckBox(self.widget1)
#        self.checkBoxSound.setObjectName("checkBoxSound")
#        self.verticalLayout_3.addWidget(self.checkBoxSound)
        
        #---- Creating a button to read the plain text edit
#        self.buttonRead = QtWidgets.QPushButton(Form)
#        self.buttonRead.setObjectName("buttonRead")
#        self.verticalLayout_3.addWidget(self.buttonRead)
        
        #----- Snooze Check Box ----
        self.checkBoxSnooze = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxSnooze.setObjectName("checkBoxSnooze")
        self.verticalLayout_3.addWidget(self.checkBoxSnooze)
        
        
        
        #------ Sleep Mode Check Box -----
#        self.checkBoxSleepMode = QtWidgets.QCheckBox(self.widget1)
#        self.checkBoxSleepMode.setObjectName("checkBoxSleepMode")
#        self.verticalLayout_3.addWidget(self.checkBoxSleepMode)
#        
#        #---- MonitorPower Check Box ------
#        self.checkBoxMonitorPower = QtWidgets.QCheckBox(self.widget1)
#        self.checkBoxMonitorPower.setObjectName("checkBoxMonitorPower")
#        self.verticalLayout_3.addWidget(self.checkBoxMonitorPower)
#        self.widget2 = QtWidgets.QWidget(Form)
#        self.widget2.setGeometry(QtCore.QRect(230, 440, 161, 21))
#        self.widget2.setObjectName("widget2")
        
        #------ Horizontal Slider ----
#        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
#        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#        self.horizontalSlider = QtWidgets.QSlider(self.widget2)
#        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
#        self.horizontalSlider.setObjectName("horizontalSlider")
#        self.horizontalSlider.setMaximum(100)
#        self.horizontalSlider.setMinimum(0)
#        self.horizontalSlider.setValue(50)
#        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        
#        #------ Volume Label Percentage ------
#        self.labelVol = QtWidgets.QLabel(self.widget2)
#        self.labelVol.setObjectName("labelVol")
#        self.horizontalLayout_2.addWidget(self.labelVol)
#        
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(20, 570, 381, 31))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        #------ Button Ok ------
        self.buttonOk = QtWidgets.QPushButton(self.widget3)
        self.buttonOk.setObjectName("buttonOk")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icon/alarm-636561.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOk.setIcon(icon)
        self.horizontalLayout_3.addWidget(self.buttonOk)
        
        #----- Button Cancel -----
        self.buttonCancel = QtWidgets.QPushButton(self.widget3)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_3.addWidget(self.buttonCancel)
        
        self.widget4 = QtWidgets.QWidget(Form)
        self.widget4.setGeometry(QtCore.QRect(20, 410, 281, 26))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        #------ Spin Sound To Select Music ------
#        self.spinSound = QtWidgets.QSpinBox(self.widget4)
#        self.spinSound.setReadOnly(False)
#        self.spinSound.setObjectName("spinSound")
#        self.horizontalLayout_4.addWidget(self.spinSound)
        self.comboBoxSound = QtWidgets.QComboBox(self.widget4)
        self.comboBoxSound.setObjectName("comboBoxSound")
        self.horizontalLayout_4.addWidget(self.comboBoxSound)
        
        #------ Button Play to Select the Sound ----
        self.buttonPlay = QtWidgets.QPushButton(self.widget4)
        self.buttonPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("icon/play-video-play-start-audio-play-914.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon1)
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout_4.addWidget(self.buttonPlay)
       
        
        #----- Button to search for the music that you like 
        self.buttonBrowse = QtWidgets.QPushButton(self.widget4)
        self.buttonBrowse.setObjectName("buttonBrowse")
        self.horizontalLayout_4.addWidget(self.buttonBrowse)
        
        # Creating a button to print all the Alarm Created
#        self.buttonPrint = QtWidgets.QPushButton(Form);
#        self.buttonPrint.setObjectName("buttonPrint");
#        self.horizontalLayout_3.addWidget(self.buttonPrint)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        #--- Reading the check Box Text
#        self.monday = self.checkBoxMon.text()
#        self.tuesday = self.checkBoxTues.text()
#        self.wednesday = self.checkBoxWed.text()
#        self.thursday = self.checkBoxThurs.text()
#        self.friday = self.checkBoxFri.text()
#        self.saturday = self.checkBoxSat.text()
#        self.sunday = self.checkBoxSun.text()
#        
#        
#        #Reading the checkbox after the state changed
#        self.checkBoxMon.stateChanged.connect(lambda: self.readCheckBox(self.monday))
#        self.checkBoxTues.stateChanged.connect(lambda: self.readCheckBox(self.tuesday))
#        self.checkBoxWed.stateChanged.connect(lambda: self.readCheckBox(self.wednesday))
#        self.checkBoxThurs.stateChanged.connect(lambda: self.readCheckBox(self.thursday))
#        self.checkBoxFri.stateChanged.connect(lambda: self.readCheckBox(self.friday))
#        self.checkBoxSat.stateChanged.connect(lambda: self.readCheckBox(self.saturday))
#        self.checkBoxSun.stateChanged.connect(lambda: self.readCheckBox(self.sunday))
        
        #Creating a self-checklist to check how many days want to repeat
#        self.checkList  = []
#        for i in range(1,8):
#            self.checkList.append(False)
        
        
        # Connect the cancel button the quit method
#        self.buttonCancel.clicked.connect(self.cancelWidget)
#        self.buttonCancel.clicked.connect(self.showAlarmDialog)
        
        # Connect to the read button
#        self.buttonRead.clicked.connect(self.readPlainText)
        
        # Creating a list of days 
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        
        # Creating an AlarmList
        self.alarmListDesktop = AlarmList();
               
        # Connect to the Pushbutton Ok 
        self.buttonOk.clicked.connect(lambda:self.OkWidget(Form))
        
        # Add multiple strings to the combox
        self.MusicalList = MusicList.musicList()
        self.comboBoxSound.addItems(self.MusicalList.fileList)
        
        # Connecting the playbutton to the selectMusic method
        self.songText = self.comboBoxSound.currentText()
        self.comboBoxSound.currentTextChanged.connect(self.selectMusic)
        
        # Connect the buttonPlay to playMusicGUI method
        self.buttonPlay.clicked.connect(self.playMusicGUI)
        
        # get the buttonBrowse connect to the browseMusic method
        self.buttonBrowse.clicked.connect(lambda:self.browseMusic(Form))
        
        ## Setting the current threding is not running
#        self.running = False;
#        self.running2 = False;
#        self.lock = threading.Lock()
#        self.lock2 = threading.Lock()
#        
#        #When the signal is sent, generate this equations
#        self.finished.connect(lambda:self.showAlarmDialog(Form))
        
        #Connect the Snooze to a SpinBox that has a value between 1 to 10 minutes
        self.checkBoxSnooze.stateChanged.connect(self.snoozeSpinBox)
        
        #Assigning the Snooze Value = False;
        self.snoozeOptions = False
        self.snoozeValue = 0
#        self.start = False
        
        # Hiding the widgets
        self.buttonCancel.clicked.connect(lambda: self.cancelWidget(Form))
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Label:"))
        self.groupBox.setTitle(_translate("Form", "Time"))
        self.label.setText(_translate("Form", "Hour"))
        self.label_2.setText(_translate("Form", "Minute"))
        self.groupBox_2.setTitle(_translate("Form", "Repeat"))
        self.checkBoxMon.setText(_translate("Form", "Monday"))
        self.checkBoxTues.setText(_translate("Form", "Tuesday"))
        self.checkBoxWed.setText(_translate("Form", "Wednesday"))
        self.checkBoxThurs.setText(_translate("Form", "Thursday"))
        self.checkBoxFri.setText(_translate("Form", "Friday"))
        self.checkBoxSat.setText(_translate("Form", "Saturday"))
        self.checkBoxSun.setText(_translate("Form", "Sunday"))
#        self.checkBoxVol.setText(_translate("Form", "Turn On The Volume"))
#        self.checkBoxSound.setText(_translate("Form", "Repeat Sound"))
        self.checkBoxSnooze.setText(_translate("Form", "Snooze"))
#        self.checkBoxSleepMode.setText(_translate("Form", "Wake up computer from sleep mode"))
#        self.checkBoxMonitorPower.setText(_translate("Form", "Turn on the monitor power"))
#        self.buttonRead.setText(_translate("Form", "Read"))
#        self.buttonPrint.setText(_translate("Form", "Print Alarm"))
#        self.labelVol.setText(_translate("Form", "0%"))
        self.buttonOk.setText(_translate("Form", "Ok"))
        self.buttonCancel.setText(_translate("Form", "Cancel"))
        self.buttonBrowse.setText(_translate("Form", "Browse..."))
        
    # Creating a method to receive the datename for the instant
    def readCheckBox(self,checkList):
        
        if self.checkBoxMon.isChecked():
            checkList[0] = True
            
        elif self.checkBoxMon.checkState != True:
            checkList[0] = False
            
        if self.checkBoxTues.isChecked():
            checkList[1] = True
                
        elif self.checkBoxTues.checkState != True:
            checkList[1] = False
            
        if self.checkBoxWed.isChecked():
            checkList[2] = True
            
        elif self.checkBoxWed.checkState != True:
            checkList[2] = False
        
        if self.checkBoxThurs.isChecked():
            checkList[3] = True
            
        elif self.checkBoxThurs.checkState != True:
            checkList[3] = False
            
        if self.checkBoxFri.isChecked():
            checkList[4] = True
            
        elif self.checkBoxFri.checkState != True:
            checkList[4] = False
        
        if self.checkBoxSat.isChecked():
            checkList[5] = True
            
        elif self.checkBoxSat.checkState != True:
            checkList[5] = False
            
        if self.checkBoxSun.isChecked():
            checkList[6] = True
            
        elif self.checkBoxSun.checkState != True:
            checkList[6] = False
            
            
    #----- Cancel Widget ------ 
    def cancelWidget(self,Form):
        Form.hide()
        pass
    
    #---------- OkWidget --------
    def OkWidget(self,Form):
        
        if self.alarmListDesktop.getaddAlarmSettingOn() == True:
            checkList = []
            for i in range(7):
                checkList.append(False);
                    
            self.readCheckBox(checkList)
            #reading the Hour
            self.hour = self.spinHour.value()
            #Reading the minute
            self.minute = self.spinMinute.value()
            # Return the Note of the Alarm
            self.info = self.plainTextEdit.toPlainText();
            
            # Return the name of the song
            self.songText = self.comboBoxSound.currentText()
                
            #  Return the value of the spinbox
            if self.checkBoxSnooze.isChecked():
                self.snoozeValue = self.spinboxSnooze.value();
            else:
                pass
                
                
            # Receive what dayy it should be repeated
        #       for i in range(len(self.checkList)):
        #           if self.checkList[i] == True:
                
        #- Creating an Alarm object 
            alarmClock = Alarm(self.hour,self.minute,self.info,checkList,self.songText,self.snoozeOptions,self.snoozeValue);
            self.alarmListDesktop.addAlarm(alarmClock)
                        
        #       alarmClock = Alarm(self.hour,self.minute,self.info,song = self.songText, snooze = self.snoozeOptions,snoozeValue = self.snoozeValue);
        #       self.alarmListDesktop.addAlarm(alarmClock)
            self.alarmListDesktop.checkAlarmList()
            self.alarmListDesktop.setaddAlarmSettingOff()
                
#            print("New List")
#        
#            for index in range(self.alarmListDesktop.alarmNumber):
#                print(self.alarmListDesktop.alarmList[index].getAlarm()); print(self.alarmListDesktop.alarmList[index].title,self.alarmListDesktop.alarmList[index].song);
        
        else:
            pass
        
        if self.alarmListDesktop.getEditAlarmSetting() == True:
            for alarmObject in self.alarmListDesktop.alarmList:
                if alarmObject.getEditMode() == False:
                    pass
                    
                elif alarmObject.getEditMode() == True:
                    checkList = []
                    for i in range(7):
                        checkList.append(False);
                            
                    self.readCheckBox(checkList)
                    #reading the Hour
                    self.hour = self.spinHour.value()
                    #Reading the minute
                    self.minute = self.spinMinute.value()
                    # Return the Note of the Alarm
                    self.info = self.plainTextEdit.toPlainText();
                    
                    # Return the name of the song
                    self.songText = self.comboBoxSound.currentText()
                        
                    #  Return the value of the spinbox
                    if self.checkBoxSnooze.isChecked():
                        self.snoozeMode = True
                        self.snoozeValue = self.spinboxSnooze.value();
                    else:
                        self.snoozeMode = False
                        self.snoozeValue = 0
                    
                    alarmObject.editAlarm(self.hour,self.minute,self.info,checkList,self.songText,self.snoozeMode,self.snoozeValue)
                    alarmObject.setEditModeOff()
                    
                    print("New List")
                    
#                    for index in range(self.alarmListDesktop.alarmNumber):
#                        print(self.alarmListDesktop.alarmList[index].getAlarm()); print(self.alarmListDesktop.alarmList[index].title,self.alarmListDesktop.alarmList[index].song);
                        
                self.alarmListDesktop.setEditAlarmSettingOff();
                
        else:
            pass;
                    
                    
                    
                    
                    
                
                
            # Receive what dayy it should be repeated
        #       for i in range(len(self.checkList)):
        #           if self.checkList[i] == True:
                
        #- Creating an Alarm object 
#        alarmClock = Alarm(self.hour,self.minute,self.info,checkList,self.songText,self.snoozeOptions,self.snoozeValue);
#        self.alarmListDesktop.addAlarm(alarmClock)
#                        
#        #       alarmClock = Alarm(self.hour,self.minute,self.info,song = self.songText, snooze = self.snoozeOptions,snoozeValue = self.snoozeValue);
#        #       self.alarmListDesktop.addAlarm(alarmClock)
#        self.alarmListDesktop.checkAlarmList()
#                    
        
        
#        self.running2 = True;
#        #Threading to check
#        if self.running2 == True and self.alarmListDesktop.checkingStatus == False:
#            t1 = threading.Thread(target = AlarmOn, args = (self.alarmListDesktop,self.MusicalList))
#            t1.start()
#            print("2 Running")
#        else:
#            print("2 Not Running")
        
        # Set the condition of self running to True to confirm that the thread is running
#        self.running = True 
#        if self.running == True and self.start == False:
#            self.start = True
#            t2 = threading.Thread(target = self.monitorPower);
#            t2.start()
#            print("Running")
#        else:
#            print("Not Running")
        
        
        #Hiding the Form
        Form.hide();
    
    #------- Creating A QMessageBox
    def showAlarmDialog(self,Form):
        pass
                                 
#        self.msgBox = QtWidgets.QMessageBox()
#        self.msgBox.setWindowIcon(QtGui.QIcon("icon/Angry_Bird.ico"))
#        self.msgBox.setIconPixmap(QtGui.QPixmap("icon/Angry_Bird.ico"))
##        now = datetime.now()
##        now = now.strftime("%H:%M:%S")
#        title = self.alarmListDesktop.alarmList[self.alarmIndex].getTitle();
#        alarmTime = self.alarmListDesktop.alarmList[self.alarmIndex].getAlarm();
#        self.msgBox.setText(alarmTime + "\n" + title + "\n" + "This will print out a meaningful Quote that random generated from the file")
#        
#        if self.alarmListDesktop.alarmList[self.alarmIndex].checkSnooze() == True: 
#            buttonSnooze = QtWidgets.QPushButton();
#            buttonSnooze.setObjectName("buttonSnooze");
#            buttonSnooze.setText("Snooze");
#            self.msgBox.addButton(buttonSnooze,QtWidgets.QMessageBox.ActionRole)
#            #buttonSnooze.clicked.connect(self.snooze)
#            
#        elif self.alarmListDesktop.alarmList[self.alarmIndex].checkSnooze() == False:
#            pass
#        self.msgBox.setWindowTitle("Alarm")
#        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
#
#        self.returnValue = self.msgBox.exec_()
#        
#        if self.returnValue == QtWidgets.QMessageBox.Ok:
#            self.alarmListDesktop.alarmList[self.alarmIndex].stop_sound();
#            self.alarmListDesktop.deleteAlarm(self.alarmListDesktop.alarmList[self.alarmIndex]);
#            print("Alarm List: ")
#            for index in range(self.alarmListDesktop.alarmNumber):
#                print(self.alarmListDesktop.alarmList[index].getAlarm()); print(self.alarmListDesktop.alarmList[index].title,self.alarmListDesktop.alarmList[index].song);
#            
#            
#            self.running = True
#            if self.running == True and self.start == False:
#                self.start = True
#                t2 = threading.Thread(target = self.monitorPower);
#                t2.start()
#                print("Running")
#            else:
#                print("Not Running")
#                
#        else:
#            self.alarmListDesktop.alarmList[self.alarmIndex].stop_sound();
#            self.alarmListDesktop.alarmList[self.alarmIndex].snoozeMethod();
#            print("Alarm List: ")
#            for index in range(self.alarmListDesktop.alarmNumber):
#                print(self.alarmListDesktop.alarmList[index].getAlarm()); print(self.alarmListDesktop.alarmList[index].title,self.alarmListDesktop.alarmList[index].song);
#                
#            self.running = True
#            if self.running == True and self.start == False:
#                self.start = True
#                t2 = threading.Thread(target = self.monitorPower);
#                t2.start()
#                print("Running")
#            else:
#                print("Not Running")
                    
            
    # Read Spin Hour
#    def readSpinBox(self):
#        # Reading the spinHour
#        self.hour = self.spinHour.value()
#        
#        #Reading the Spin Minute
#        self.minute = self.spinMinute.value()
    
    # Print all the Alarm
    def printWidget(self):
        for index in range(len(self.alarmListDesktop)):
            print(self.alarmListDesktop.alarmList[index].getAlarm())
        
    #Read Plain Text
#    def readPlainText(self):
#        self.info = self.plainTextEdit.toPlainText()
#        pass
    
    #Read The Sound
    def readSpinSound(self):
        pass
    
    #Adjust the volume
#    def adjustVol(self,value):
#        self.labelVol.setText(str(value) + "%")
#        Volume = value/100
#        mixer.music.set_volume(Volume)
#        pass
            
    #---- Creating a snooze Spinbox ------
    def snoozeSpinBox(self):
        
        if self.checkBoxSnooze.isChecked():
            self.spinboxSnooze = QtWidgets.QSpinBox();
            self.spinboxSnooze.setReadOnly(False)
            self.spinboxSnooze.setObjectName("spinMinute")
            #Setting spinMinute range from 0 -> 10
            self.spinboxSnooze.setRange(1,10)
            self.verticalLayout_3.insertWidget(1,self.spinboxSnooze)
            self.snoozeLabel = QtWidgets.QLabel("Snooze Minute")
            self.verticalLayout_3.insertWidget(1,self.snoozeLabel)
            
            # Creating a snooze options
            self.snoozeOptions = True;
            self.snoozeValue = self.spinboxSnooze.value();
        
        elif self.checkBoxSnooze.checkState != True:
            self.spinboxSnooze.deleteLater()
            self.snoozeLabel.deleteLater()
            
            # Seting a snoozeOptions back to False and value back to 0
            self.snoozeOptions = False;
            self.snoozeValue = 0;
            
        
        
    #Alarm is still on during sleep mode
    def SleepMode(self):
        pass
    
    # Turning on the Alarm when the alarm goes on
    def monitorPower(self):
        pass
        
#        for alarmObject_Music in self.alarmListDesktop.alarmList:
#            if alarmObject_Music.music_running == True:
#                musicPlay = alarmObject_Music.music_running;
#        while self.running == True and self.start == True:
#            self.lock.acquire()
#            for alarmObject in self.alarmListDesktop.alarmList:
#                if alarmObject.getMusicStatus() == True:
#                    self.alarmIndex = self.alarmListDesktop.alarmList.index(alarmObject)
#                    #self.alarmObject = alarmObject;
#                    self.running = False
#                    self.start = False
##                    if alarmObject.checkRepeatStatus() == False and alarmObject.checkSnooze() == False:
##                        self.alarmListDesktop.deleteAlarm(alarmObject);
#                    
#            self.lock.release()
#            
#        print("Stop Running")
#        
#        if self.running == False and self.start == False:
#            self.finished.emit()
    
    
            
        
    #---------
    def selectMusic(self):
        self.songText = self.comboBoxSound.currentText()

    def playMusicGUI(self):
        self.MusicalList.playSong(self.songText)
        
    def browseMusic(self,Form):
        song = QtWidgets.QFileDialog.getOpenFileName(Form, 'Open File', 'self.MusicalList.root','Sound Files(*.mp3 *.ogg *.wav *.m4a)')
        print(song[0])
        if song[0]:
            filename = Path(song[0]).name
            self.comboBoxSound.addItem(filename);
            self.MusicalList.addSong(song[0])
        
        

        

#if __name__ == "__main__":
#    import sys
#    app = QtCore.QCoreApplication.instance()
#    if app is None:
#        app = QtWidgets.QApplication(sys.argv)
#    app.setQuitOnLastWindowClosed(False)
#    Form = QtWidgets.QWidget()
#    ui = Ui_Form()
#    ui.setupUi(Form)
#    Form.show()
#    sys.exit(app.exec_())
