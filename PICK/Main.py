import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from GUI_Subsystem.PICK_GUI import Ui_MainWindow
from GUI_Subsystem.filter import filterPopup
from GUI_Subsystem.icons import IconConfigDialog
from Directory_Configuration import Directory_config
from Event_Configuration import Event_config
from Team_Configuration import Team_config
from Splunk.Splunk import Splunk_Class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        #Declare config classes variables
        self.dirConfig = Directory_config()
        self.eventConfig = Event_config(self.dirConfig)
        self.teamConfig = Team_config(self.eventConfig)

        #Configure Main Buttons
        self.centWid = self.findChild(QtWidgets.QWidget,'centralwidget')
        self.filtButt = self.centWid.findChild(QtWidgets.QPushButton,'LogEntryFilterBut')
        self.filtButt.clicked.connect(self.showFilter)
        self.graphViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'GraphViewIconConfigBut')
        self.doubViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'DoubleViewIconConfigBut')
        self.graphViewIconButt.clicked.connect(self.showIcons)
        self.doubViewIconButt.clicked.connect(self.showIcons)
        self.eventConfigButt = self.findChild(QtWidgets.QAction,'actionEvent_Configuration_2')
        self.eventConfigButt.triggered.connect(self.eventConfig.showEventConfig)
        self.dirConfigButt = self.findChild(QtWidgets.QAction,'actionDir_Configuration')
        self.dirConfigButt.triggered.connect(self.dirConfig.showDirectoryConfig)
        self.teamConfigButt = self.findChild(QtWidgets.QAction,'actionTeam_Configuration')
        self.teamConfigButt.triggered.connect(self.teamConfig.showTeamConfig)
        

        #Splunk INstance
        self.splunker = Splunk_Class()

        #COnnect Directory Ingestion with button here
        self.dirConfig.DirecConfig.findChild(QtWidgets.QPushButton, 'SaveEventBut').clicked.connect(self.startIngestion)

        #Initialize Views
        self.teamConfig.showTeamConfig()

    def startIngestion(self):
        if(self.dirConfig.checkFolders()):
            self.dirConfig.DirecConfig.close()
            self.show()
            self.readLogFiles()


    #Method to show filter popup
    def showFilter(self):
        exPopup = filterPopup(self)
        exPopup.show()

    def showIcons(self):
        exPopup = IconConfigDialog(self)
        exPopup.show()


#Method to read files and put them into log file in the table
    def readLogFiles(self):
        #We get log file table and log entry table
        self.logFTable = self.centWid.findChild(QtWidgets.QTableWidget,'logFileTable')

        #Insert White File in File Table
        rowPosition = self.logFTable.rowCount()
        self.logFTable.insertRow(rowPosition)
        self.logFTable.setItem(rowPosition , 0, QTableWidgetItem("testWhite.txt"))
        self.logFTable.setItem(rowPosition , 1, QTableWidgetItem(self.dirConfig.whiteFolder))
        self.logFTable.setItem(rowPosition , 2, QTableWidgetItem("Non Cleansed"))
        self.logFTable.setItem(rowPosition , 3, QTableWidgetItem("Non Validated"))
        self.logFTable.setItem(rowPosition , 4, QTableWidgetItem("Non Ingested"))

        #Insert Blue File in File Table
        rowPosition = self.logFTable.rowCount()
        self.logFTable.insertRow(rowPosition)
        self.logFTable.setItem(rowPosition , 0, QTableWidgetItem("blueTest.txt"))
        self.logFTable.setItem(rowPosition , 1, QTableWidgetItem(self.dirConfig.blueFolder))
        self.logFTable.setItem(rowPosition , 2, QTableWidgetItem("Non Cleansed"))
        self.logFTable.setItem(rowPosition , 3, QTableWidgetItem("Non Validated"))
        self.logFTable.setItem(rowPosition , 4, QTableWidgetItem("Non Ingested"))

        #Insert Red File in File Table
        rowPosition = self.logFTable.rowCount()
        self.logFTable.insertRow(rowPosition)
        self.logFTable.setItem(rowPosition , 0, QTableWidgetItem("redTest.txt"))
        self.logFTable.setItem(rowPosition , 1, QTableWidgetItem(self.dirConfig.redFolder))
        self.logFTable.setItem(rowPosition , 2, QTableWidgetItem("Non Cleansed"))
        self.logFTable.setItem(rowPosition , 3, QTableWidgetItem("Non Validated"))
        self.logFTable.setItem(rowPosition , 4, QTableWidgetItem("Non Ingested"))



        #Method that demoes the splunk behavior
    def uploadToSplunk(self):
        self.logETable = self.centWid.findChild(QtWidgets.QTableWidget,'LogEntryTable')
        #Upload files to splunk
        self.splunker.uploadFiles(self.dirConfig.whiteFolder,"white_team")
        self.splunker.uploadFiles(self.dirConfig.redFolder,"red_team")
        self.splunker.uploadFiles(self.dirConfig.blueFolder,"blue_team")

    def searchFromSplunk(self):
        #Read files from splunk
        index = "white_team"
        filters = {
            "startTime":"",
            "endTime":"2020-03-31 22:00:00",
            "keywords":""
        }
        self.logEntries = self.splunker.search(index,filters)

        #Show files obtained from Splunk
        for log in self.logEntries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

    def viewEnforcementReport(self):
        self.enforceTab = self.centWid.findChild(QtWidgets.QTableWidget,'logFileErrorsTable')
        rowPosition = self.enforceTab.rowCount()
        self.enforceTab.insertRow(rowPosition)
        self.enforceTab.setItem(rowPosition,0,QTableWidgetItem("testBlue.txt"))
        self.enforceTab.setItem(rowPosition,1,QTableWidgetItem("Line 4"))
        self.enforceTab.setItem(rowPosition,2,QTableWidgetItem("Invalid Character Found"))


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
app.exec()
