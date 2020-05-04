import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QFileInfo
from pathlib import Path

from GUI_Subsystem.Directory_GUI import Ui_DirectoryConfig

class Directory_config(object):
    blueFolder=""
    whiteFolder=""
    redFolder = ""
    rootFolder = ""

    def __init__(self, *args, obj=None, **kwargs):
        self.null = 0
        self.DirecConfig = QtWidgets.QWidget()
        ui = Ui_DirectoryConfig()
        ui.setupUi(self.DirecConfig)
        self.directConfigLogic()

    #Sets event configuration to be able to show it again to go back
    def setEventConfig(self,eConfig):
        self.eConfig = eConfig

    #Sets button's logic in directory configuration
    def directConfigLogic(self):
        self.DirecConfig.findChild(QtWidgets.QPushButton,'ReddirectBut').clicked.connect(self.setRedDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton,'BluedirectBut').clicked.connect(self.setBlueDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton,'RootdirectBut').clicked.connect(self.setRootDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton,'WhitedirectBut').clicked.connect(self.setWhiteDirect)
        self.DirecConfig.findChild(QtWidgets.QPushButton, 'goBackToEvent').clicked.connect(self.goBackToEvent)
        

    #Action when button to save directory config is clicked, check if folders are set, if not throw error
    def saveDirectConfig(self):
        try: self.rootFolder
        except AttributeError: 
            QMessageBox.about(self.DirecConfig, "Error", "Root Folder not Defined")
        else:         
            #Check folders inside root folder
            root=self.rootFolder
            dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
            if(len(dirlist)==3 and ('White Team' in dirlist) and ('Blue Team' in dirlist) and ('Red Team' in dirlist)):
                #folder structure is correct
                self.setWhiteDirect(self.rootFolder+'/White Team')
                self.setRedDirect(self.rootFolder+'/Red Team')
                self.setBlueDirect(self.rootFolder+'/Blue Team')
            else:
                QMessageBox.about(self.DirecConfig, "Error", "Folder naming or structure incorrect")
                
    def checkFolders(self):
        try: self.rootFolder
        except AttributeError: 
            QMessageBox.about(self.DirecConfig, "Error", "Root Folder not Defined")
            return False
        else:
            return True


    #Set root directory and ingest a file
    def setRootDirect(self):
        self.rootFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.rootTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'RootDirectTextbox')
        self.rootTextBox.setPlainText(self.rootFolder)
        self.saveDirectConfig()

    #Set white team directory 
    def setWhiteDirect(self,name):
        #self.whiteFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.whiteFolder = name
        self.whiteTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'whiteTeamTextbox')
        self.whiteTextBox.setPlainText(self.whiteFolder)

    #Set red team directory 
    def setRedDirect(self,name):
        #self.redFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.redFolder = name
        self.redTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'RedTeamtextbox')
        self.redTextBox.setPlainText(self.redFolder)


    #Set blue team directory
    def setBlueDirect(self,name):
        #self.blueFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.blueFolder = name
        self.blueTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'BlueTeamTextbox')
        self.blueTextBox.setPlainText(self.blueFolder)

    def showDirectoryConfig(self):
        self.DirecConfig.show()

    def goBackToEvent(self):
        self.eConfig.showEventConfig()
        self.DirecConfig.close()