import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from GUI_Subsystem.Team_Configuration_GUI import Ui_TeamConfiguration
from Event_Configuration import Event_config

class Team_config(object):
    def __init__(self,econfig, *args, obj=None, **kwargs):
        self.eventConfir = econfig
        self.TeamConfiguration = QtWidgets.QWidget()
        ui = Ui_TeamConfiguration()
        ui.setupUi(self.TeamConfiguration)
        self.teamConfigLogic()

    def showTeamConfig(self):
        self.TeamConfiguration.show()

    def teamConfigLogic(self):
        self.TeamConfiguration.findChild(QtWidgets.QPushButton, 'TeamConfigurationButtonConnect').clicked.connect(self.saveTeamConfig)

    def saveTeamConfig(self):
        self.eventConfir.setTeamConfig(self)
        self.eventConfir.showEventConfig()
        self.TeamConfiguration.close()