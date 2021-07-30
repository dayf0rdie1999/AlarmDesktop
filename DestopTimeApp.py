# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesktopTimeApp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AlarmSettingGUI import Ui_Form
import threading
from Alarm import AlarmOn
from TimerGUI import Ui_TimerForm
from StopWatchUi import Ui_StopWatchForm
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
            base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_MainWindow(QtCore.QObject):
    finished = QtCore.pyqtSignal();
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 602)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        MainWindow.setToolTipDuration(-3)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 981, 561))
        self.widget.setObjectName("widget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        
        #----- Adding Alarm Button
        self.pushButton = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icon/add-439817.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        #---- Removing Alarm Button
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("icon/remove-667650.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        #---- Editting the Alarm
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("icon/editing-edit-343335.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        #---- Recreating the same alarm
#        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
#        icon3 = QtGui.QIcon()
#        icon3.addPixmap(QtGui.QPixmap("icon/repo-clone-24524.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#        self.pushButton_4.setIcon(icon3)
#        self.pushButton_4.setObjectName("pushButton_4")
#        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.frame)
        
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        
#        self.item = QtWidgets.QListWidgetItem(self.listWidget)
#        self.listWidget.addItem(self.item)
#        
#        #--- Creating a CustomWidget
#        self.row = MyCustomWidget("Foo")
#        self.item.setSizeHint(self.row.minimumSizeHint())
#        self.listWidget.setItemWidget(self.item,self.row)
#    
#        #--- Creating a second widgets
#        self.item2 = QtWidgets.QListWidgetItem(self.listWidget)
#        self.listWidget.addItem(self.item2)
#        self.row2 = MyCustomWidget("Fap")
#        self.item2.setSizeHint(self.row2.minimumSizeHint())
#        self.listWidget.setItemWidget(self.item2,self.row2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setAutoFillBackground(True)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionOpen = QtWidgets.QAction(MainWindow)
        
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("icon/OpenFolderIcon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(resource_path("icon/file-save-517273.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(resource_path("icon/folder-hide-122174.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionTimer = QtWidgets.QAction(MainWindow)
        
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(resource_path("icon/timer-590913.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTimer.setIcon(icon7)
        self.actionTimer.setObjectName("actionTimer")
        self.actionStopWatch = QtWidgets.QAction(MainWindow)
        
        
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(resource_path("icon/stopwatch-616652.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStopWatch.setIcon(icon8)
        self.actionStopWatch.setObjectName("actionStopWatch")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionALarm = QtWidgets.QAction(MainWindow)
       
        
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(resource_path("icon/alarm-636561.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionALarm.setIcon(icon9)
        self.actionALarm.setStatusTip("")
        self.actionALarm.setObjectName("actionALarm")
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        
        self.menuSettings.addAction(self.actionTimer)
        self.menuSettings.addAction(self.actionStopWatch)
        self.menuSettings.addAction(self.actionALarm)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ## Connecting the Add button to open up the AlarmSettingGUI
        self.Form = QtWidgets.QWidget();
        self.Ui = Ui_Form();
        self.Ui.setupUi(self.Form);
        self.pushButton.clicked.connect(self.openSetting)
        
        #Connecting the Okbutton from Form Widget to activate action to the main window
        self.Ui.buttonOk.clicked.connect(self.showAlarm);
        self.Ui.buttonOk.clicked.connect(self.startThread);
        
        self.listWidget.currentItemChanged.connect(self.printIndex)
#        self.pushButton_2.clicked.connect(self.checkAlarm);
        
        # Connecting the Remove buttom from the Widget to activate the delete Alarm
        self.pushButton_2.clicked.connect(self.removeAlarm)
        
        self.clicked = False;
        self.running = False;
        self.running2 = False;
        self.lock = threading.Lock()
        self.lock2 = threading.Lock()
        self.start = False
        
        #When the signal is sent, generate this equations
        self.finished.connect(self.showAlarmDialog)
        
        
        #Connecting the edit push button to the edit method
        self.pushButton_3.clicked.connect(self.editMethod)
        
        self.StopWatchForm = QtWidgets.QWidget()
        self.ui = Ui_StopWatchForm()
        self.ui.setupUi(self.StopWatchForm)
        
        # Connecting the Timer button to the method to show the TimerGUI
        self.TimerForm = QtWidgets.QWidget()
        self.timerUi = Ui_TimerForm()
        self.timerUi.setupUi(self.TimerForm)

        self.actionTimer.triggered.connect(self.showTimerForm)

        self.actionStopWatch.triggered.connect(self.showStopWatchForm)        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit"))
#        self.pushButton_4.setText(_translate("MainWindow", "Clone"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open A File"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save a File"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save A File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Hide The Application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionTimer.setText(_translate("MainWindow", "Timer"))
        self.actionTimer.setStatusTip(_translate("MainWindow", "Set a Timer"))
        self.actionTimer.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionStopWatch.setText(_translate("MainWindow", "StopWatch"))
        self.actionStopWatch.setStatusTip(_translate("MainWindow", "Start A StopWatch"))
        self.action.setText(_translate("MainWindow", "Alarm"))
        self.actionALarm.setText(_translate("MainWindow", "Alarm"))
        self.actionALarm.setShortcut(_translate("MainWindow", "Ctrl+A"))


    def showStopWatchForm(self):
        self.StopWatchForm.show()
        
    # Show Timer Form
    def showTimerForm(self):
        self.TimerForm.show()
        
    #-- Creating a editMethod
    def editMethod(self):
        if self.clicked == True:
            self.Form.show()
            self.Ui.alarmListDesktop.setEditAlarmSettingOn();
            self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].setEditModeOn();
            #Setting the alarm hour and alarm minute
            self.Ui.spinHour.setValue(self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].hour);
            self.Ui.spinMinute.setValue(self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].minute);
            
            #Clearing the plain text edit
            self.Ui.plainTextEdit.clear();
            self.Ui.plainTextEdit.insertPlainText(self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].title);
            
            self.Ui.checkBoxSnooze.setChecked(self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkSnooze());
            
            if self.Ui.checkBoxSnooze.isChecked():
                self.Ui.spinboxSnooze.setValue(self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].snoozeValue);
            else:
                pass
            
            #Setting Monday Check Box
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[0] == True:
                self.Ui.checkBoxMon.setChecked(True);
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[0] == False:
                self.Ui.checkBoxMon.setChecked(False);
                
            #Setting Tuesday Check Box
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[1] == True:
                self.Ui.checkBoxTues.setChecked(True);
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[1] == False:
                self.Ui.checkBoxTues.setChecked(False);
                
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[2] == True:
                self.Ui.checkBoxWed.setChecked(True);
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[2] == False:
                self.Ui.checkBoxWed.setChecked(False);
                
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[3] == True:
                self.Ui.checkBoxThurs.setChecked(True);
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[3] == False:
                self.Ui.checkBoxThurs.setChecked(False);
                
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[4] == True:
                self.Ui.checkBoxFri.setChecked(True);
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[4] == False:
                self.Ui.checkBoxFri.setChecked(False);
              
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[5] == True:
                self.Ui.checkBoxSat.setChecked(True);
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[5] == False:
                self.Ui.checkBoxSat.setChecked(False);
                
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[6] == True:
                self.Ui.checkBoxSun.setChecked(True);
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkList[6] == False:
                self.Ui.checkBoxSun.setChecked(False);
            
            # Setting the snooze check box and the snooze value
            if self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkSnooze() == True:
                self.Ui.checkBoxSnooze.setChecked(True);
                self.Ui.spinboxSnooze.setValue(self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].snoozeValue)
                
            elif self.Ui.alarmListDesktop.alarmList[self.listWidget.currentRow()].checkSnooze() == False:
                self.Ui.checkBoxSnooze.setChecked(False);
                
            self.clicked = False;
        else:
            self.warningBox = QtWidgets.QMessageBox()
            self.warningBox.setWindowIcon(QtGui.QIcon(resource_path("icon/Angry_Bird.ico")))
            self.warningBox.setIconPixmap(QtGui.QPixmap(resource_path("icon/Angry_Bird.ico")))
            
            self.warningBox.setText("No Alarm Has Selected")
            
            self.warningBox.setWindowTitle("Warning")
            self.warningBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            
            signalValue = self.warningBox.exec_();
            
            if signalValue == QtWidgets.QMessageBox.Ok:
                pass
            else:
                pass
            
            
    
    #-- Creating a method to pop up the AlarmSettingsGUI
    def openSetting(self):
        self.Ui.alarmListDesktop.setaddAlarmSettingOn()
        self.Form.show();
        
        # Setting Everything into Default Mode
        self.Ui.spinHour.setValue(0);
        self.Ui.spinMinute.setValue(0);
        
        self.Ui.checkBoxMon.setChecked(False);
        self.Ui.checkBoxTues.setChecked(False);
        self.Ui.checkBoxWed.setChecked(False);
        self.Ui.checkBoxThurs.setChecked(False);
        self.Ui.checkBoxFri.setChecked(False);
        self.Ui.checkBoxSat.setChecked(False);
        self.Ui.checkBoxSun.setChecked(False);
        
        self.Ui.plainTextEdit.clear();
        self.Ui.checkBoxSnooze.setChecked(False);
        
        
        
    def showAlarm(self): 
        self.listWidget.clear();
        for alarmObject in self.Ui.alarmListDesktop.alarmList:
            item = QtWidgets.QListWidgetItem(self.listWidget)
            self.listWidget.addItem(item)
            #--- Creating a CustomWidget
            row = MyCustomWidget(alarmObject,self.Ui.alarmListDesktop,self.Ui,self.start,self.running,self.running2)
            item.setSizeHint(row.minimumSizeHint())
            self.listWidget.setItemWidget(item,row)
        
    
    def printIndex(self):
        self.clicked = True
#        print(self.listWidget.count())
#        print(self.listWidget.currentRow())
        
        
    def removeAlarm(self):
        if self.clicked == True:
            self.questionBox = QtWidgets.QMessageBox()
            self.questionBox.setWindowIcon(QtGui.QIcon(resource_path("icon/Angry_Bird.ico")))
            self.questionBox.setIconPixmap(QtGui.QPixmap(resource_path("icon/Angry_Bird.ico")))
            
            self.questionBox.setText("Do you want to delete this alarm? ")
            
            self.questionBox.setWindowTitle("Delete Alarm")
            self.questionBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            
            signalValue = self.questionBox.exec_();
            
            if signalValue == QtWidgets.QMessageBox.Ok:
                self.clicked = False
                self.deteleAlarm();
                
            else:
                pass
        else:
            self.warningBox = QtWidgets.QMessageBox()
            self.warningBox.setWindowIcon(QtGui.QIcon(resource_path("icon/Angry_Bird.ico")))
            self.warningBox.setIconPixmap(QtGui.QPixmap(resource_path("icon/Angry_Bird.ico")))
            
            self.warningBox.setText("No Alarm Has Selected")
            
            self.warningBox.setWindowTitle("Warning")
            self.warningBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            
            signalValue = self.warningBox.exec_();
            
            if signalValue == QtWidgets.QMessageBox.Ok:
                pass
            else:
                pass
      
    def deteleAlarm(self):
        self.Ui.alarmListDesktop.deleteAlarmIndex(self.listWidget.currentRow())
        self.listWidget.takeItem(self.listWidget.currentRow())
        
        for alarmObject in self.Ui.alarmListDesktop.alarmList:
            print(alarmObject.getAlarm())
        
            
    def startThread(self):
        
        self.running2 = True;
        #Threading to check
        if self.running2 == True and self.Ui.alarmListDesktop.checkingStatus == False:
            t1 = threading.Thread(target = AlarmOn, args = (self.Ui.alarmListDesktop,self.Ui.MusicalList))
            t1.start()
            print("2 Running")
        else:
            print("2 Not Running")
        
        self.running = True 
        if self.running == True and self.start == False:
            self.start = True
            t2 = threading.Thread(target = self.readsignal);
            t2.start()
            print("Running")
        else:
            print("Not Running")
    
    def readsignal(self):
        
        while self.running == True and self.start == True:
            self.lock.acquire()
            for alarmObject in self.Ui.alarmListDesktop.alarmList:
                if alarmObject.getMusicStatus() == True:
                    self.alarmIndex = self.Ui.alarmListDesktop.alarmList.index(alarmObject)
                    self.running = False
                    self.start = False
                    
            self.lock.release()
            
        print("Stop Running")
        
        if self.running == False and self.start == False:
            self.finished.emit()
    
    #---- Pop up showAlarmDialog -----
    def showAlarmDialog(self):
        
        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox.setWindowIcon(QtGui.QIcon(resource_path("icon/Angry_Bird.ico")))
        self.msgBox.setIconPixmap(QtGui.QPixmap(resource_path("icon/Angry_Bird.ico")))
#        now = datetime.now()
#        now = now.strftime("%H:%M:%S")
        title = self.Ui.alarmListDesktop.alarmList[self.alarmIndex].getTitle();
        alarmTime = self.Ui.alarmListDesktop.alarmList[self.alarmIndex].getAlarm();
        self.msgBox.setText(alarmTime + "\n" + title + "\n" + "This will print out a meaningful Quote that random generated from the file")
        
        if self.Ui.alarmListDesktop.alarmList[self.alarmIndex].checkSnooze() == True: 
            buttonSnooze = QtWidgets.QPushButton();
            buttonSnooze.setObjectName("buttonSnooze");
            buttonSnooze.setText("Snooze");
            self.msgBox.addButton(buttonSnooze,QtWidgets.QMessageBox.ActionRole)

            
        elif self.Ui.alarmListDesktop.alarmList[self.alarmIndex].checkSnooze() == False:
            pass
        self.msgBox.setWindowTitle("Alarm")
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.returnValue = self.msgBox.exec_()
        
        if self.returnValue == QtWidgets.QMessageBox.Ok:
            self.Ui.alarmListDesktop.alarmList[self.alarmIndex].resetAlarmTime();
            if self.Ui.alarmListDesktop.alarmList[self.alarmIndex].checkRepeatStatus() == False:
                self.Ui.alarmListDesktop.alarmList[self.alarmIndex].setAlarmOff();
            print("Alarm Setting is:" +  str(self.Ui.alarmListDesktop.alarmList[self.alarmIndex].checkSnooze()))
            
            self.showAlarm()
            self.Ui.alarmListDesktop.alarmList[self.alarmIndex].stop_sound();
            self.Ui.alarmListDesktop.alarmList[self.alarmIndex].checkAlarm();
            
            print("Alarm List: ")
            for index in range(self.Ui.alarmListDesktop.alarmNumber):
                print(self.Ui.alarmListDesktop.alarmList[index].getAlarm()); print(self.Ui.alarmListDesktop.alarmList[index].title,self.Ui.alarmListDesktop.alarmList[index].song);
            
            
            self.running = True
            if self.running == True and self.start == False:
                self.start = True
                t2 = threading.Thread(target = self.readsignal);
                t2.start()
                print("Running")
            else:
                print("Not Running")
                
        else:
            self.Ui.alarmListDesktop.alarmList[self.alarmIndex].stop_sound();
            self.Ui.alarmListDesktop.alarmList[self.alarmIndex].snoozeMethod();
            print("Alarm List: ")
            for index in range(self.Ui.alarmListDesktop.alarmNumber):
                print(self.Ui.alarmListDesktop.alarmList[index].getAlarm()); print(self.Ui.alarmListDesktop.alarmList[index].title,self.Ui.alarmListDesktop.alarmList[index].song);
                
            self.running = True
            if self.running == True and self.start == False: 
                self.start = True
                t2 = threading.Thread(target = self.readsignal);
                t2.start()
                print("Running")
            else:
                print("Not Running")
                
        
            

class MyCustomWidget(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self,alarmObject,alarmObjectList,Ui,start,running,running2,parent = None):
        super(MyCustomWidget, self).__init__(parent)
        self.Ui = Ui
        self.start = start
        self.running = running
        self.running = running2
        self.alarmObjectList = alarmObjectList
        self.hour = alarmObject.hour
        self.minute = alarmObject.minute
        self.info = alarmObject.getTitle()
        self.song = alarmObject.song
        self.repeatDate = alarmObject.checkRepeatDate();
        
        self.row = QtWidgets.QHBoxLayout()
        self.checkBox = QtWidgets.QCheckBox(str(self.hour) + ":" + str(self.minute) + "\n" + self.repeatDate);
        self.row.addWidget(self.checkBox)
        self.row.addWidget(QtWidgets.QLabel(self.info))
        self.row.addWidget(QtWidgets.QLabel(self.song))
        self.setLayout(self.row)
        
        if alarmObject.getAlarmStatus() == True:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        #-- Connecting the check box into the Alarm
        self.checkBox.stateChanged.connect(lambda: self.setAlarm(Ui))
        
        
    
    def setAlarm(self,Ui):
        if self.checkBox.isChecked() == True:
            for alarmObject in self.alarmObjectList.alarmList:
                if alarmObject.getHour() == self.hour and alarmObject.getMinute() == self.minute and alarmObject.getTitle() == self.info:
                    alarmObject.checkAlarm();
                    alarmObject.setAlarmOn();
                    
            self.running2 = True;
            #Threading to check
            if self.running2 == True and self.alarmObjectList.checkingStatus == False:
                t1 = threading.Thread(target = AlarmOn, args = (self.alarmObjectList,self.Ui.MusicalList))
                t1.start()
                print("2 Running")
            else:
                print("2 Not Running")
                    

        
        elif self.checkBox.checkState != True:
            for alarmObject in self.alarmObjectList.alarmList:
                if alarmObject.getHour() == self.hour and alarmObject.getMinute() == self.minute and alarmObject.getTitle() == self.info:
                    alarmObject.setAlarmOff();
                      

    
    def setCheckBoxOff(self,alarmObject):
        self.checkBox.setChecked(False);
        
    def setCheckBoxOn(self):
        self.checkBox.setChecked(True);
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
