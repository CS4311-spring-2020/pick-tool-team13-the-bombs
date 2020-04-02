import sys
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
    def __init__(self, *args, obj=None, **kwargs):
        self.null = 0


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
            QMessageBox.about(self.DirecConfig, "Error", "Root Folder not Defined")
        try: self.whiteFolder
        except AttributeError: 
            QMessageBox.about(self.DirecConfig, "Error", "White Team Folder not Defined")
        try: self.blueFolder
        except AttributeError: 
            QMessageBox.about(self.DirecConfig, "Error", "Blue Team Folder not Defined")
        try: self.redFolder
        except AttributeError: 
            QMessageBox.about(self.DirecConfig, "Error", "Red Team Folder not Defined")
        else:         
            #save directories in a file for now
            f= open("C:\\Users\\vcone\\Desktop\\Cosas\\CS\\Software2\\GUI test\\pick-tool-team13-the-bombs\\PICK\\Project_Configuration\\directories.txt","w+")
            f.write(self.rootFolder + "\n")
            f.write(self.redFolder + "\n")
            f.write(self.blueFolder + "\n")
            f.write(self.whiteFolder + "\n")
            f.close()
            self.DirecConfig.close()


    #Set root directory and ingest a file
    def setRootDirect(self):
        self.rootFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.rootTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'RootDirectTextbox')
        self.rootTextBox.setPlainText(self.rootFolder)

    #Set white team directory 
    def setWhiteDirect(self):
        self.whiteFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.whiteTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'whiteTeamTextbox')
        self.whiteTextBox.setPlainText(self.whiteFolder)

    #Set red team directory 
    def setRedDirect(self):
        self.redFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.redTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'RedTeamtextbox')
        self.redTextBox.setPlainText(self.redFolder)


    #Set blue team directory
    def setBlueDirect(self):
        self.blueFolder = QtWidgets.QFileDialog.getExistingDirectory(self.DirecConfig,'Select Directory')
        self.blueTextBox = self.DirecConfig.findChild(QtWidgets.QTextBrowser,'BlueTeamTextbox')
        self.blueTextBox.setPlainText(self.blueFolder)

    def showDirectoryConfig(self):
        self.DirecConfig = QtWidgets.QWidget()
        ui = Ui_DirectoryConfig()
        ui.setupUi(self.DirecConfig)
        self.directConfigLogic()
        self.DirecConfig.show()
