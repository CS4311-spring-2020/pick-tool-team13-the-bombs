# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeamConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TeamConfiguration(object):
    def setupUi(self, TeamConfiguration):
        TeamConfiguration.setObjectName("TeamConfiguration")
        TeamConfiguration.resize(900, 700)
        TeamConfiguration.setMinimumSize(QtCore.QSize(900, 700))
        TeamConfiguration.setMaximumSize(QtCore.QSize(900, 700))
        self.TeamConfiguration_Title = QtWidgets.QLabel(TeamConfiguration)
        self.TeamConfiguration_Title.setGeometry(QtCore.QRect(310, 30, 291, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TeamConfiguration_Title.setFont(font)
        self.TeamConfiguration_Title.setObjectName("TeamConfiguration_Title")
        self.TeamConfigurationIPTextBox = QtWidgets.QPlainTextEdit(TeamConfiguration)
        self.TeamConfigurationIPTextBox.setGeometry(QtCore.QRect(330, 180, 231, 51))
        self.TeamConfigurationIPTextBox.setObjectName("TeamConfigurationIPTextBox")
        self.TeamConfigurationLeadCheckBox = QtWidgets.QCheckBox(TeamConfiguration)
        self.TeamConfigurationLeadCheckBox.setGeometry(QtCore.QRect(390, 260, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TeamConfigurationLeadCheckBox.setFont(font)
        self.TeamConfigurationLeadCheckBox.setObjectName("TeamConfigurationLeadCheckBox")
        self.TeamConfigurationEstablished = QtWidgets.QLabel(TeamConfiguration)
        self.TeamConfigurationEstablished.setGeometry(QtCore.QRect(230, 280, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TeamConfigurationEstablished.setFont(font)
        self.TeamConfigurationEstablished.setObjectName("TeamConfigurationEstablished")
        self.TeamConfigurationLabelNumber = QtWidgets.QLabel(TeamConfiguration)
        self.TeamConfigurationLabelNumber.setGeometry(QtCore.QRect(430, 360, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TeamConfigurationLabelNumber.setFont(font)
        self.TeamConfigurationLabelNumber.setObjectName("TeamConfigurationLabelNumber")
        self.TeamConfigurationButtonConnect = QtWidgets.QPushButton(TeamConfiguration)
        self.TeamConfigurationButtonConnect.setGeometry(QtCore.QRect(370, 410, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TeamConfigurationButtonConnect.setFont(font)
        self.TeamConfigurationButtonConnect.setObjectName("TeamConfigurationButtonConnect")

        self.retranslateUi(TeamConfiguration)
        QtCore.QMetaObject.connectSlotsByName(TeamConfiguration)

    def retranslateUi(self, TeamConfiguration):
        _translate = QtCore.QCoreApplication.translate
        TeamConfiguration.setWindowTitle(_translate("TeamConfiguration", "Form"))
        self.TeamConfiguration_Title.setText(_translate("TeamConfiguration", "Team Configuration"))
        self.TeamConfigurationLeadCheckBox.setText(_translate("TeamConfiguration", "Lead"))
        self.TeamConfigurationEstablished.setText(_translate("TeamConfiguration", "No. of established connections to the lead\'s IP address:"))
        self.TeamConfigurationLabelNumber.setText(_translate("TeamConfiguration", "0"))
        self.TeamConfigurationButtonConnect.setText(_translate("TeamConfiguration", "Connect"))
