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
from Data_Processing.Log_File import Log_File
from Data_Processing.Enforcement_Action_Report import Enforcement

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        #Declare filter popup and set buttons
        self.filters = filterPopup()
        self.filters.buttonBox.accepted.connect(self.filterEntries)
        self.filters.buttonBox.rejected.connect(self.closeFilter)

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
        
        #Some tables
        self.logETable = self.centWid.findChild(QtWidgets.QTableWidget,'LogEntryTable')

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
            self.readLogFiles(self.dirConfig.whiteFolder)
            self.readLogFiles(self.dirConfig.blueFolder)
            self.readLogFiles(self.dirConfig.whiteFolder)
            self.populateLogEntryTable()

    #Method to show filter popup
    def showFilter(self):
        self.filters.show()
    #Method to close filter popup without doing anything
    def closeFilter(self):
        self.filters.close()

    #Method to search in splunk with filters from the filter popup
    def filterEntries(self):
        index = "*"
        keywords = str(self.filters.keyWordSearch.text())
        startTime = self.filters.startTime.dateTime().toString("yyyy-MM-ddThh:mm:ss")
        endTime = self.filters.endTime.dateTime().toString("yyyy-MM-ddThh:mm:ss")
        if(self.filters.redBox.isChecked() == True or self.filters.redBox2.isChecked() == True):
            index = "red_team"
        elif(self.filters.whiteBox.isChecked() == True or self.filters.whiteBox2.isChecked() == True):
            index = "white_team"
        elif(self.filters.blueBox.isChecked() == True or self.filters.blueBox2.isChecked() == True):
            index = "blue_team"

        filters = {
            "startTime":startTime,
            "endTime":endTime,
            "keywords":keywords
        }
        entries = self.splunker.search(index,filters)
        self.populateEntryTable(entries)

    def showIcons(self):
        exPopup = IconConfigDialog(self)
        exPopup.show()


#Method to read files and put them into log file in the table
    def readLogFiles(self,dir):
        #We get log file table to show files with errors
        self.logFTable = self.centWid.findChild(QtWidgets.QTableWidget,'logFileTable')
        
        #We create our list of Log Files
        self.logFiles = []

        #Now we populate list of log files here
        for filename in os.listdir(dir):
            self.logFiles.append(Log_File(filename))
        
        #For each log file we get we attempt to cleanse
        for file in self.logFiles:
            file.cleanseFile()
            if(not file.cleansed):
                #We send it to enforcement action report
                self.viewEnforcementReport(file)

        #We upload files that were cleansed
        #FIXME For now we just upload files in folder
        self.uploadToSplunk(dir)

        #Method that demoes the splunk behavior
    def uploadToSplunk(self,dir):
        #We check what the directory is to select proper place to upload
        if(os.path.basename(dir)=="Blue Team"):
            index = "blue_team"
        elif(os.path.basename(dir)=="Red Team"):
            index = "red_team"
        elif(os.path.basename(dir)=="White Team"):
            index = "white_team"
        #Upload files to splunk
        self.splunker.uploadFiles(dir,index)

    def searchFromSplunk(self,searchIndex):
        #Read files from splunk
        index = searchIndex
        filters = {
            "startTime":"",
            "endTime":"",
            "keywords":""
        }
        self.logEntries = self.splunker.search(index,filters)

        #Show files obtained from Splunk
        for log in self.logEntries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +" "+ log[3] +" "+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

    #Method that populates the log entry table with proper log entries for demo
    #FIXME is for demo
    def populateLogEntryTable(self):
        
        filters = {
            "startTime":"",
            "endTime":"",
            "keywords":""
        }
        whiteEntries = self.splunker.search("white_team",filters)
        blueEntries = self.splunker.search("blue_team",filters)
        redEntries = self.splunker.search("red_team",filters)
        #Show files obtained from Splunk
        for log in whiteEntries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +"\n"+ log[3] +"\n"+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

        #Show files obtained from Splunk
        for log in redEntries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +"\n"+ log[3] +"\n"+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

                #Show files obtained from Splunk
        for log in blueEntries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +"\n"+ log[3] +"\n"+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

    def populateEntryTable(self,entries):
        for log in entries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +"\n"+ log[3] +"\n"+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
app.exec()
