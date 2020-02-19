# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'Event.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class eventConfiguration(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("self")
        self.resize(1171, 680)
        self.EventTitlelabel = QtWidgets.QLabel(self)
        self.EventTitlelabel.setGeometry(QtCore.QRect(390, 20, 421, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.EventTitlelabel.setFont(font)
        self.EventTitlelabel.setObjectName("EventTitlelabel")
        self.NameTextbox = QtWidgets.QTextBrowser(self)
        self.NameTextbox.setGeometry(QtCore.QRect(210, 130, 241, 111))
        self.NameTextbox.setObjectName("NameTextbox")
        self.EventNamelabel = QtWidgets.QLabel(self)
        self.EventNamelabel.setGeometry(QtCore.QRect(40, 150, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventNamelabel.setFont(font)
        self.EventNamelabel.setObjectName("EventNamelabel")
        self.EventStartTextbox = QtWidgets.QTextBrowser(self)
        self.EventStartTextbox.setGeometry(QtCore.QRect(840, 130, 241, 111))
        self.EventStartTextbox.setObjectName("EventStartTextbox")
        self.EventStartlabel = QtWidgets.QLabel(self)
        self.EventStartlabel.setGeometry(QtCore.QRect(580, 170, 226, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventStartlabel.setFont(font)
        self.EventStartlabel.setObjectName("EventStartlabel")
        self.DescriptionTextbox = QtWidgets.QTextBrowser(self)
        self.DescriptionTextbox.setGeometry(QtCore.QRect(210, 390, 241, 111))
        self.DescriptionTextbox.setObjectName("DescriptionTextbox")
        self.EventDescriptionlabel = QtWidgets.QLabel(self)
        self.EventDescriptionlabel.setGeometry(QtCore.QRect(30, 420, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventDescriptionlabel.setFont(font)
        self.EventDescriptionlabel.setObjectName("EventDescriptionlabel")
        self.EventEndTextbox = QtWidgets.QTextBrowser(self)
        self.EventEndTextbox.setGeometry(QtCore.QRect(840, 400, 241, 111))
        self.EventEndTextbox.setObjectName("EventEndTextbox")
        self.EventEndlabel = QtWidgets.QLabel(self)
        self.EventEndlabel.setGeometry(QtCore.QRect(580, 440, 216, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventEndlabel.setFont(font)
        self.EventEndlabel.setObjectName("EventEndlabel")
        self.SaveEventBut = QtWidgets.QPushButton(self)
        self.SaveEventBut.setGeometry(QtCore.QRect(650, 570, 483, 28))
        self.SaveEventBut.setObjectName("SaveEventBut")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.EventTitlelabel.setText(_translate("self", "Event Configuration"))
        self.EventNamelabel.setText(_translate("self", "Event Name"))
        self.EventStartlabel.setText(_translate("self", "Event Start timestamp"))
        self.EventDescriptionlabel.setText(_translate("self", "Event Description"))
        self.EventEndlabel.setText(_translate("self", "Event End timestamp"))
        self.SaveEventBut.setText(_translate("self", "Save Event"))

