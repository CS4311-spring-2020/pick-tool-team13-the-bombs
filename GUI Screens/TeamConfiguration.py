# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:47:52 2020
@author: Eduardo
UI:https://www.youtube.com/watch?v=LaoU_o50u9k
"""

import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow,  QAction, qApp
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import EventDirectory

class TeamConfig(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Team configuration'
        self.left = 10              #starting position from the left of the screen to the app
        self.top = 50               #start position from the top of the screen to the app
        self.width = 1250            #size
        self.height = 800           #size
        self.connectButton = QtWidgets.QPushButton('Connect',self)
        self.initUI()
    
    def initUI(self):
        
        #Team Configuration
        self.TeamConfiguration()
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
       
    def TeamConfiguration(self):
        
        #Title
        WindowTitle = QtWidgets.QLabel("Team Configuration",self)
        #WindowTitle.setText("Event Configuration                        ")
        WindowTitle.move(((self.width/2)-108),50) 
        WindowTitle.setMinimumSize(280,0)           #Is going to have 280 width of text
        WindowTitle.setFont(QtGui.QFont("Roboto",20, QtGui.QFont.Bold))
        
        #Checkbox if Lead
        LeadCheck = QtWidgets.QCheckBox("Lead",self)
        LeadCheck.move(((self.width/2)+155),150)         #pixes below the name so it looks like being in the same margin
        
        #Lead IP Address Label
        LeadLabel = QtWidgets.QLabel(self)
        LeadLabel.setText("Lead IP Address")
        LeadLabel.setMinimumSize(280,0)           #Is going to have 280 width of text
        LeadLabel.move(((self.width/2)-157),145)
        LeadLabel.setFont(QtGui.QFont("Roboto",12, QtGui.QFont.Helvetica))
        
        #Lead IP address text
        LeadIPAdd = QtWidgets.QLineEdit(self)
        LeadIPAdd.move(((self.width/2)-28),150)         #pixes below the name so it looks like being in the same margin
        LeadIPAdd.resize(140,28)
        LeadIPAdd.setFont(QtGui.QFont("Roboto",11, QtGui.QFont.Helvetica))
        
        #Label of established Connections
        estabIP = QtWidgets.QLabel(self)
        estabIP.setText("No. of established connections to the lead's IP address:")
        estabIP.setMinimumSize(370,0)
        estabIP.move(((self.width/2)-155),200)         #pixes below the name so it looks like being in the same margin
        estabIP.setFont(QtGui.QFont("Roboto",11, QtGui.QFont.Helvetica))
        
        #Number of Established connections
        numConnected = QtWidgets.QLabel(self)
        numConnected.setText("0")
        numConnected.move(((self.width/2)+20),225)
        numConnected.setFont(QtGui.QFont("Roboto",11, QtGui.QFont.Helvetica))
        
        #button with the connections
        #connectButton = QtWidgets.QPushButton('Connect',self)
        self.connectButton.move(((self.width/2)-20),370)
        
        self.connectButton.clicked.connect(self.changeWindow)
        
        
    def changeWindow(self):
        window = EventDirectory()
        window.show()
        self.close()
       
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TeamConfig()
    sys.exit(app.exec_())