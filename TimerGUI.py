# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Timer import Timer
from datetime import datetime
import threading
import time
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

class Ui_TimerForm(QtCore.QObject):
    
    def setupUi(self, TimerForm):
        TimerForm.setObjectName("TimerForm")
        TimerForm.resize(338, 284)
        TimerForm.setStyleSheet("background-color: rgb(0, 170, 255);")
#        TimerForm.resize(TimerForm.sizeHint().width,TimerForm.size().height() + self.horizontalLayout.sizeHint().height());
        
        self.timerLabel = QtWidgets.QLabel(TimerForm)
        self.timerLabel.setGeometry(QtCore.QRect(60, 40, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.timerLabel.setFont(font)
        self.timerLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timerLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timerLabel.setScaledContents(True)
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")
        
        self.startTimer = QtWidgets.QPushButton(TimerForm)
        self.startTimer.setGeometry(QtCore.QRect(250, 190, 71, 61))
        self.startTimer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startTimer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icon/Angry, Bird, Black, Frame, Red png icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startTimer.setIcon(icon)
        self.startTimer.setIconSize(QtCore.QSize(128, 128))
        self.startTimer.setObjectName("startTimer")
        
        self.widget = QtWidgets.QWidget(TimerForm)
        self.widget.setGeometry(QtCore.QRect(30, 190, 211, 61))
        self.widget.setObjectName("widget")
        
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        
        #Setting the value for the spinBOx
        self.spinBox.setRange(0,23)
        
        self.verticalLayout.addWidget(self.spinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        
        #Setting the range value for the spinBox_2
        self.spinBox_2.setRange(0,59)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_3)
        
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_3.setObjectName("spinBox_3")
        
        #Setting the range value for the self.spinBox_3
        self.spinBox_3.setRange(0,59);
        
        self.verticalLayout_3.addWidget(self.spinBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        
        self.stopTimer = QtWidgets.QPushButton(TimerForm)
        self.stopTimer.setGeometry(QtCore.QRect(250, 190, 71, 61))
        self.stopTimer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stopTimer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icon/GreenPigFrame.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopTimer.setIcon(icon)
        self.stopTimer.setIconSize(QtCore.QSize(80, 80))
        self.stopTimer.setObjectName("startTimer")
        self.horizontalLayout.addWidget(self.stopTimer)
        
#        TimerForm.resize(TimerForm.sizeHint().width,TimerForm.size().height() + self.horizontalLayout.sizeHint().height());
        

        self.retranslateUi(TimerForm)
        QtCore.QMetaObject.connectSlotsByName(TimerForm)
        
        #Connecting the Button to the Angry Bird Image
        self.startTimer.clicked.connect(self.setTimer);
    
        self.stopTimer.clicked.connect(self.stopTimer_Method);
        
    def retranslateUi(self, TimerForm):
        _translate = QtCore.QCoreApplication.translate
        TimerForm.setWindowTitle(_translate("TimerForm", "Timer"))
        self.timerLabel.setText(_translate("TimerForm", "00:00:00"));
        self.label.setText(_translate("TimerForm", "Hour"))
        self.label_2.setText(_translate("TimerForm", "Minute"))
        self.label_3.setText(_translate("TimerForm", "Second"))

    def stopTimer_Method(self):
        self.TimeStart = False;
        self.Timer.setTimeWatch();
        self.timerLabel.setText(self.Timer.getStrTimeWatch())
        
    def setTimer(self):
        self.hour = self.spinBox.value();
        self.fixedHour = self.hour;
        self.minute = self.spinBox_2.value();
        self.fixedMinute = self.minute;
        self.second = self.spinBox_3.value();
        self.fixedSecond = self.second
        
        
        self.Timer = Timer(self.hour,self.minute,self.second)
        
        self.timerLabel.setText(self.Timer.getStrTimeWatch())
        
        self.running = True 
        if self.running == True:
            t2 = threading.Thread(target = self.runTime);
            t2.start()
            print("Running")
        else:
            print("Not Running")
      
     
    def runTime(self):
        self.TimeStart = True
        while self.TimeStart == True:
            if self.second == 0:
                self.second = 59
                self.minute -= 1
                
            if self.minute == 0 and self.hour != 0:
                self.hour -= 1
                self.minute = 59
                
            time.sleep(1)  
            self.second -= 1
            self.Timer.checkTimeWatch(self.hour,self.minute,self.second);
            
            self.timerLabel.setText(self.Timer.getStrTimeWatch())
            
            if self.hour == self.minute == self.second == 0:
                self.TimeStart = False;
        

#if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    TimerForm = QtWidgets.QWidget()
##    ui = Ui_TimerForm()
##    ui.setupUi(TimerForm)
##    TimerForm.show()
##    sys.exit(app.exec_())
