# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StopWatchUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from StopWatch import StopWatch
import threading
import time
from datetime import datetime


class Ui_StopWatchForm(object):
    def setupUi(self, StopWatchForm):
        StopWatchForm.setObjectName("StopWatchForm")
        StopWatchForm.resize(531, 390)
        StopWatchForm.setStyleSheet("background-color: rgb(170, 85, 127);")
        
        self.label = QtWidgets.QLabel(StopWatchForm)
        self.label.setGeometry(QtCore.QRect(130, 30, 271, 111))
        
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.listWidget = QtWidgets.QListWidget(StopWatchForm)
        self.listWidget.setGeometry(QtCore.QRect(20, 220, 491, 151))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        
        self.widget = QtWidgets.QWidget(StopWatchForm)
        self.widget.setGeometry(QtCore.QRect(20, 160, 491, 51))
        self.widget.setObjectName("widget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pushButton_Start = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.horizontalLayout.addWidget(self.pushButton_Start)
        
        self.pushButton_Pause = QtWidgets.QPushButton(self.widget)
        self.pushButton_Pause.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_Pause.setObjectName("pushButton_Pause")
        self.horizontalLayout.addWidget(self.pushButton_Pause)
        
        self.pushButton_Catch = QtWidgets.QPushButton(self.widget)
        self.pushButton_Catch.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_Catch.setObjectName("pushButton_Catch")
        self.horizontalLayout.addWidget(self.pushButton_Catch)
        
        self.pushButton_Stop = QtWidgets.QPushButton(self.widget)
        self.pushButton_Stop.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.horizontalLayout.addWidget(self.pushButton_Stop)

        self.retranslateUi(StopWatchForm)
        QtCore.QMetaObject.connectSlotsByName(StopWatchForm)
        
        self.pushButton_Start.clicked.connect(self.startStopWatch)
        self.pushButton_Stop.clicked.connect(self.stopStopWatch)
        self.pushButton_Pause.clicked.connect(self.pauseStopWatch)
        self.pushButton_Catch.clicked.connect(self.catchTime)
        
        self.objectCreated = False;
        
    def retranslateUi(self, StopWatchForm):
        _translate = QtCore.QCoreApplication.translate
        StopWatchForm.setWindowTitle(_translate("StopWatchForm", "Form"))
        self.label.setText(_translate("StopWatchForm", "00:00:00"))
        self.pushButton_Start.setText(_translate("StopWatchForm", "Start"))
        self.pushButton_Pause.setText(_translate("StopWatchForm", "Pause"))
        self.pushButton_Catch.setText(_translate("StopWatchForm", "Catch"))
        self.pushButton_Stop.setText(_translate("StopWatchForm", "Stop"))
        
    
    def startStopWatch(self):
        if self.objectCreated == False:
            self.stopWatch = StopWatch();
            self.objectCreated = True
        else:
            pass
        
        self.running = True
        if self.running == True:
            t1 = threading.Thread(target = self.startTime);
            t1.start()
            print("Running") 
        else:
            print("Not Running")
            
    def startTime(self):
        self.stopWatch.TimeStart = True
        while self.stopWatch.TimeStart == True:
            time.sleep(0.001)
            self.stopWatch.milisecond += 1000
            self.stopWatch.startTime()
            
            if  self.stopWatch.milisecond == 999000:
                self.stopWatch.milisecond = 0;
                self.stopWatch.second += 1;
                
            if  self.stopWatch.second == 59:
                self.stopWatch.second = 0
                self.stopWatch.minute += 1
                
            if self.stopWatch.minute == 59:
                self.stopWatch.hour += 1
                self.stopWatch.minute = 0
            
            self.label.setText(self.stopWatch.getStrTimeWatch())
            
    def stopStopWatch(self):
        self.objectCreated = False
        self.stopWatch.resetTime();
        self.label.setText(self.stopWatch.getStrTimeWatch())
        
    def pauseStopWatch(self):
        self.stopWatch.pauseStopWatch();

    def catchTime(self):
        self.listWidget.addItem(self.stopWatch.getStrTimeWatch())

#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    StopWatchForm = QtWidgets.QWidget()
#    ui = Ui_StopWatchForm()
#    ui.setupUi(StopWatchForm)
#    StopWatchForm.show()
#    sys.exit(app.exec_())
