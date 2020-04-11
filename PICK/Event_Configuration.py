import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QDateTime

from GUI_Subsystem.Event_GUI import Ui_EventConfig
from Directory_Configuration import Directory_config

class Event_config(object):
    def __init__(self,dconfig, *args, obj=None, **kwargs):
        self.dirConfig = dconfig
        self.EventConfig = QtWidgets.QWidget()
        ui = Ui_EventConfig()
        ui.setupUi(self.EventConfig)
        self.eventConfigLogic()

    def showEventConfig(self):
        self.EventConfig.show()

    def eventConfigLogic(self):
        self.EventConfig.findChild(QtWidgets.QPushButton, 'saveEventButt').clicked.connect(self.saveEventConfig)
        self.EventConfig.findChild(QtWidgets.QPushButton, 'goToDirConfigButt').clicked.connect(self.moveToDirectConfig)

    def saveEventConfig(self):
        #Save event Stuff in a file for now
        if(self.checkDates()):
            QMessageBox.about(self.EventConfig, "Success", "Dates are correct")
        else:
            QMessageBox.about(self.EventConfig, "Error", "Start Date is bigger than end date")

    def checkDates(self):
        self.startDate = self.EventConfig.findChild(QtWidgets.QDateTimeEdit,'EventConfigStartDate').dateTime()
        self.endDate = self.EventConfig.findChild(QtWidgets.QDateTimeEdit,'EventConfigEndDate').dateTime()
        if (self.startDate > self.endDate):
            return False
        return True

    def moveToDirectConfig(self):
        self.dirConfig.showDirectoryConfig()
        self.EventConfig.close()