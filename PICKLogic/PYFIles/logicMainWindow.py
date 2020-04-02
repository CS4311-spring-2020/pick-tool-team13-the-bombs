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
