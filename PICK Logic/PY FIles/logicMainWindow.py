import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from PICKGUI import Ui_MainWindow
from filter import filterPopup
from icons import IconConfigDialog
from Event import Ui_EventConfig
from Directory import Ui_DirectoryConfig

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


    def directConfigLogic(self):
        self.DirecConfig.findChild(QtWidgets.QPushButton, 'SaveEventBut').clicked.connect(self.saveDirectConfig)
    
    def saveDirectConfig(self):
        self.showEventConfig()
        self.DirecConfig.close()

    def showDirectoryConfig(self):
        self.DirecConfig = QtWidgets.QWidget()
        ui = Ui_DirectoryConfig()
        ui.setupUi(self.DirecConfig)
        self.directConfigLogic()
        self.DirecConfig.show()




app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()