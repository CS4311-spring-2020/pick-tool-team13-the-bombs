import sys
sys.path.insert(1,'../')
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QFileInfo
from pathlib import Path

from PICKGUI import Ui_MainWindow
from filter import filterPopup
from icons import IconConfigDialog 
from Event import Ui_EventConfig
from Directory import Ui_DirectoryConfig
from Splunk.SplunkUploader import SplunkUploader

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.centWid = self.findChild(QtWidgets.QWidget,'centralwidget')
        self.filtButt = self.centWid.findChild(QtWidgets.QPushButton,'LogEntryFilterBut')
        self.filtButt.clicked.connect(self.showFilter)
        self.graphViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'GraphViewIconConfigBut')
        self.doubViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'DoubleViewIconConfigBut')
        self.graphViewIconButt.clicked.connect(self.showIcons)
        self.doubViewIconButt.clicked.connect(self.showIcons)

        self.eventConfigButt = self.findChild(QtWidgets.QAction,'actionEvent_Configuration_2')
        self.eventConfigButt.triggered.connect(self.showEventConfig)
        self.validateBut = self.centWid.findChild(QtWidgets.QPushButton,'logFileConfigValidBut')
        self.validateBut.clicked.connect(self.splunkDemo)
        self.enforceViewBut = self.centWid.findChild(QtWidgets.QPushButton,'logFileConfigEnforce')
        self.enforceViewBut.clicked.connect(self.viewEnforcementReport)

        self.showDirectoryConfig()

    #Method to show filter popup
    def showFilter(self):
        exPopup = filterPopup(self)
        exPopup.show()

    def showIcons(self):
        exPopup = IconConfigDialog(self)
        exPopup.show()

    def showEventConfig(self):
        self.EventConfig = QtWidgets.QWidget()
        ui = Ui_EventConfig()
        ui.setupUi(self.EventConfig)
        self.eventConfigLogic()
        self.EventConfig.show()

    def eventConfigLogic(self):
        self.EventConfig.findChild(QtWidgets.QPushButton, 'saveEventButt').clicked.connect(self.saveEventConfig)

    def saveEventConfig(self):
        self.EventConfig.close()

    #Sets button's logic in directory configuration
    def directConfigLogic(self):
        self.DirecConfig.findChild(QtWidgets.QPushButton,'ReddirectBut').clicked.connect(self.setRedDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton,'BluedirectBut').clicked.connect(self.setBlueDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton,'RootdirectBut').clicked.connect(self.setRootDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton,'WhitedirectBut').clicked.connect(self.setWhiteDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton, 'SaveEventBut').clicked.connect(self.saveDirectConfig)

    #Action when button to save directory config is clicked, check if folders are set, if not throw error
    def saveDirectConfig(self):
        try: self.rootFolder
        except AttributeError: 
            QMessageBox.about(self, "Error", "Root Folder not Defined")
        try: self.whiteFolder
        except AttributeError: 
            QMessageBox.about(self, "Error", "White Team Folder not Defined")
        try: self.blueFolder
        except AttributeError: 
            QMessageBox.about(self, "Error", "Blue Team Folder not Defined")
        try: self.redFolder
        except AttributeError: 
            QMessageBox.about(self, "Error", "Red Team Folder not Defined")
        else: 
            self.readLogFiles()
            self.showEventConfig()
            self.DirecConfig.close()

    #Set root directory and ingest a file
    def setRootDirect(self):
        self.rootFolder = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Directory')

    #Set white team directory 
    def setWhiteDirect(self):
        self.whiteFolder = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Directory')

    #Set red team directory 
    def setRedDirect(self):
        self.redFolder = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Directory')


    #Set blue team directory
    def setBlueDirect(self):
        self.blueFolder = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Directory')

    #Show directory configuration window
    def showDirectoryConfig(self):
        self.DirecConfig = QtWidgets.QWidget()
        ui = Ui_DirectoryConfig()
        ui.setupUi(self.DirecConfig)
        self.directConfigLogic()
        self.DirecConfig.show()

    #Method to read files and put them into log file in the table
    def readLogFiles(self):
        #We will read one file from each directory for the demo purposes
        #We get log file table and log entry table
        self.logFTable = self.centWid.findChild(QtWidgets.QTableWidget,'logFileTable')


        #Read from White Folder
        whiteFile = open(self.whiteFolder+"/testWhite.txt")
        whiteContent = whiteFile.read()
        #Read from Red Folder
        redFile = open(self.redFolder+"/redTest.txt")
        redContent = redFile.read()
        #Read from Blue Folder
        blueFile = open(self.blueFolder+"/blueTest.txt")
        blueContent = blueFile.read()

        #Insert White File in File Table
        rowPosition = self.logFTable.rowCount()
        self.logFTable.insertRow(rowPosition)
        self.logFTable.setItem(rowPosition , 0, QTableWidgetItem("testWhite.txt"))
        self.logFTable.setItem(rowPosition , 1, QTableWidgetItem(self.whiteFolder))
        self.logFTable.setItem(rowPosition , 2, QTableWidgetItem("Non Cleansed"))
        self.logFTable.setItem(rowPosition , 3, QTableWidgetItem("Non Validated"))
        self.logFTable.setItem(rowPosition , 4, QTableWidgetItem("Non Ingested"))

        #Insert Blue File in File Table
        rowPosition = self.logFTable.rowCount()
        self.logFTable.insertRow(rowPosition)
        self.logFTable.setItem(rowPosition , 0, QTableWidgetItem("testBlue.txt"))
        self.logFTable.setItem(rowPosition , 1, QTableWidgetItem(self.blueFolder))
        self.logFTable.setItem(rowPosition , 2, QTableWidgetItem("Non Cleansed"))
        self.logFTable.setItem(rowPosition , 3, QTableWidgetItem("Non Validated"))
        self.logFTable.setItem(rowPosition , 4, QTableWidgetItem("Non Ingested"))

        #Insert Red File in File Table
        rowPosition = self.logFTable.rowCount()
        self.logFTable.insertRow(rowPosition)
        self.logFTable.setItem(rowPosition , 0, QTableWidgetItem("testRed.txt"))
        self.logFTable.setItem(rowPosition , 1, QTableWidgetItem(self.redFolder))
        self.logFTable.setItem(rowPosition , 2, QTableWidgetItem("Non Cleansed"))
        self.logFTable.setItem(rowPosition , 3, QTableWidgetItem("Non Validated"))
        self.logFTable.setItem(rowPosition , 4, QTableWidgetItem("Non Ingested"))


    #Method that demoes the splunk behavior
    def splunkDemo(self):
        self.logETable = self.centWid.findChild(QtWidgets.QTableWidget,'LogEntryTable')
        #Upload files to splunk
        self.splunker = SplunkUploader()
        self.splunker.uploadFiles(self.whiteFolder,"test_index")
        
        #Read files from splunk
        self.logEntries = self.splunker.readEntries("test_index")

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
window.show()
app.exec()