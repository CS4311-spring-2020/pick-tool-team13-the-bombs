from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Class for filter Popup
class filterPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filterConfiguration = QLabel("Filter Configuration",self)
        self.filterConfiguration.setFont(QtGui.QFont("Roboto",12, QtGui.QFont.Bold))

        self.creatorLabel = QLabel("Creator", self)
        self.creatorLabel.setFont(QtGui.QFont("Roboto",12, QtGui.QFont.Bold))

        self.eventType = QLabel("Event Type", self)
        self.eventType.setFont(QtGui.QFont("Roboto",12, QtGui.QFont.Bold))

        self.keyWordSearch = QLineEdit(self) #Key Word text
        self.redBox = QCheckBox(self)     #Red Check Box
        self.blueBox = QCheckBox(self)    #Blue Check Box
        self.whiteBox = QCheckBox(self)   #White Check Box
        self.redBox2 = QCheckBox(self)     #Red Check Box
        self.blueBox2 = QCheckBox(self)    #Blue Check Box
        self.whiteBox2 = QCheckBox(self)   #White Check Box
        self.startTime = QDateTimeEdit(self)  #Start time text
        self.endTime = QDateTimeEdit(self)    #End Time text
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.formGroupBox = QGroupBox("ihjnrsdijn")
        layout = QFormLayout(self)
        layout.addRow(self.filterConfiguration)
        layout.addRow("Keyword Search:", self.keyWordSearch)
        layout.addRow(self.creatorLabel)
        layout.addRow("Red", self.redBox)
        layout.addRow("Blue", self.blueBox)
        layout.addRow("White", self.whiteBox)
        layout.addRow(self.eventType)
        layout.addRow("Red", self.redBox2)
        layout.addRow("Blue", self.blueBox2)
        layout.addRow("White", self.whiteBox2)
        layout.addRow("Start TimeStamp:", self.startTime)
        layout.addRow("End TimeStamp:", self.endTime)
        layout.addWidget(self.buttonBox)

    def setDT(self, startDT = "2000-01-01T00:00:00", endDT = "2000-01-01T00:00:00",):
        self.startTime.setDateTime(QtCore.QDateTime.fromString(startDT, "yyyy-MM-ddThh:mm:ss"))
        self.endTime.setDateTime(QtCore.QDateTime.fromString(endDT, "yyyy-MM-ddThh:mm:ss"))
