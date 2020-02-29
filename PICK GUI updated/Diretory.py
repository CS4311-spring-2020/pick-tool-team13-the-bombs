# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'Directory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class directoryConfig(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("self")
        self.resize(1171, 681)
        self.DirectoryTitle = QtWidgets.QLabel(self)
        self.DirectoryTitle.setGeometry(QtCore.QRect(340, 40, 491, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DirectoryTitle.setFont(font)
        self.DirectoryTitle.setObjectName("DirectoryTitle")
        self.RootDirectlabel = QtWidgets.QLabel(self)
        self.RootDirectlabel.setGeometry(QtCore.QRect(50, 160, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RootDirectlabel.setFont(font)
        self.RootDirectlabel.setObjectName("RootDirectlabel")
        self.RootDirectTextbox = QtWidgets.QTextBrowser(self)
        self.RootDirectTextbox.setGeometry(QtCore.QRect(210, 140, 241, 111))
        self.RootDirectTextbox.setObjectName("RootDirectTextbox")
        self.RootdirectBut = QtWidgets.QPushButton(self)
        self.RootdirectBut.setGeometry(QtCore.QRect(470, 180, 93, 28))
        self.RootdirectBut.setObjectName("RootdirectBut")
        self.BlueTeamTextbox = QtWidgets.QTextBrowser(self)
        self.BlueTeamTextbox.setGeometry(QtCore.QRect(810, 140, 241, 111))
        self.BlueTeamTextbox.setObjectName("BlueTeamTextbox")
        self.BluedirectBut = QtWidgets.QPushButton(self)
        self.BluedirectBut.setGeometry(QtCore.QRect(1060, 180, 93, 28))
        self.BluedirectBut.setObjectName("BluedirectBut")
        self.BlueTeamlabel = QtWidgets.QLabel(self)
        self.BlueTeamlabel.setGeometry(QtCore.QRect(620, 180, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BlueTeamlabel.setFont(font)
        self.BlueTeamlabel.setObjectName("BlueTeamlabel")
        self.RedTeamtextbox = QtWidgets.QTextBrowser(self)
        self.RedTeamtextbox.setGeometry(QtCore.QRect(210, 400, 241, 111))
        self.RedTeamtextbox.setObjectName("RedTeamtextbox")
        self.RedTeamlabel = QtWidgets.QLabel(self)
        self.RedTeamlabel.setGeometry(QtCore.QRect(20, 430, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RedTeamlabel.setFont(font)
        self.RedTeamlabel.setObjectName("RedTeamlabel")
        self.ReddirectBut = QtWidgets.QPushButton(self)
        self.ReddirectBut.setGeometry(QtCore.QRect(470, 450, 93, 28))
        self.ReddirectBut.setObjectName("ReddirectBut")
        self.WhiteTeamLabel = QtWidgets.QLabel(self)
        self.WhiteTeamLabel.setGeometry(QtCore.QRect(610, 440, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WhiteTeamLabel.setFont(font)
        self.WhiteTeamLabel.setObjectName("WhiteTeamLabel")
        self.whiteTeamTextbox = QtWidgets.QTextBrowser(self)
        self.whiteTeamTextbox.setGeometry(QtCore.QRect(810, 400, 241, 111))
        self.whiteTeamTextbox.setObjectName("whiteTeamTextbox")
        self.WhitedirectBut = QtWidgets.QPushButton(self)
        self.WhitedirectBut.setGeometry(QtCore.QRect(1060, 450, 91, 28))
        self.WhitedirectBut.setObjectName("WhitedirectBut")
        self.SaveEventBut_2 = QtWidgets.QPushButton(self)
        self.SaveEventBut_2.setGeometry(QtCore.QRect(390, 560, 381, 91))
        self.SaveEventBut_2.setObjectName("SaveEventBut_2")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.DirectoryTitle.setText(_translate("self", "Directory Configuration"))
        self.RootDirectlabel.setText(_translate("self", "Root Directory"))
        self.RootdirectBut.setText(_translate("self", "...."))
        self.BluedirectBut.setText(_translate("self", "...."))
        self.BlueTeamlabel.setText(_translate("self", "Blue Team Folder"))
        self.RedTeamlabel.setText(_translate("self", "Red Team Folder"))
        self.ReddirectBut.setText(_translate("self", "...."))
        self.WhiteTeamLabel.setText(_translate("self", "White Team Folder"))
        self.WhitedirectBut.setText(_translate("self", "...."))
        self.SaveEventBut_2.setText(_translate("self", "Start Data Ingestion"))
        self.SaveEventBut_2.clicked.connect(self.startDataIngestion)

    def startDataIngestion(self):
        self.close()
