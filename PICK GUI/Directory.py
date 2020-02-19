# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 681)
        self.DirectoryTitle = QtWidgets.QLabel(Form)
        self.DirectoryTitle.setGeometry(QtCore.QRect(340, 40, 491, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DirectoryTitle.setFont(font)
        self.DirectoryTitle.setObjectName("DirectoryTitle")
        self.RootDirectlabel = QtWidgets.QLabel(Form)
        self.RootDirectlabel.setGeometry(QtCore.QRect(50, 160, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RootDirectlabel.setFont(font)
        self.RootDirectlabel.setObjectName("RootDirectlabel")
        self.RootDirectTextbox = QtWidgets.QTextBrowser(Form)
        self.RootDirectTextbox.setGeometry(QtCore.QRect(210, 140, 241, 111))
        self.RootDirectTextbox.setObjectName("RootDirectTextbox")
        self.RootdirectBut = QtWidgets.QPushButton(Form)
        self.RootdirectBut.setGeometry(QtCore.QRect(470, 180, 93, 28))
        self.RootdirectBut.setObjectName("RootdirectBut")
        self.BlueTeamTextbox = QtWidgets.QTextBrowser(Form)
        self.BlueTeamTextbox.setGeometry(QtCore.QRect(810, 140, 241, 111))
        self.BlueTeamTextbox.setObjectName("BlueTeamTextbox")
        self.BluedirectBut = QtWidgets.QPushButton(Form)
        self.BluedirectBut.setGeometry(QtCore.QRect(1060, 180, 93, 28))
        self.BluedirectBut.setObjectName("BluedirectBut")
        self.BlueTeamlabel = QtWidgets.QLabel(Form)
        self.BlueTeamlabel.setGeometry(QtCore.QRect(620, 180, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BlueTeamlabel.setFont(font)
        self.BlueTeamlabel.setObjectName("BlueTeamlabel")
        self.RedTeamtextbox = QtWidgets.QTextBrowser(Form)
        self.RedTeamtextbox.setGeometry(QtCore.QRect(210, 400, 241, 111))
        self.RedTeamtextbox.setObjectName("RedTeamtextbox")
        self.RedTeamlabel = QtWidgets.QLabel(Form)
        self.RedTeamlabel.setGeometry(QtCore.QRect(20, 430, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RedTeamlabel.setFont(font)
        self.RedTeamlabel.setObjectName("RedTeamlabel")
        self.ReddirectBut = QtWidgets.QPushButton(Form)
        self.ReddirectBut.setGeometry(QtCore.QRect(470, 450, 93, 28))
        self.ReddirectBut.setObjectName("ReddirectBut")
        self.WhiteTeamLabel = QtWidgets.QLabel(Form)
        self.WhiteTeamLabel.setGeometry(QtCore.QRect(610, 440, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WhiteTeamLabel.setFont(font)
        self.WhiteTeamLabel.setObjectName("WhiteTeamLabel")
        self.whiteTeamTextbox = QtWidgets.QTextBrowser(Form)
        self.whiteTeamTextbox.setGeometry(QtCore.QRect(810, 400, 241, 111))
        self.whiteTeamTextbox.setObjectName("whiteTeamTextbox")
        self.WhitedirectBut = QtWidgets.QPushButton(Form)
        self.WhitedirectBut.setGeometry(QtCore.QRect(1060, 450, 91, 28))
        self.WhitedirectBut.setObjectName("WhitedirectBut")
        self.SaveEventBut_2 = QtWidgets.QPushButton(Form)
        self.SaveEventBut_2.setGeometry(QtCore.QRect(390, 560, 381, 91))
        self.SaveEventBut_2.setObjectName("SaveEventBut_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DirectoryTitle.setText(_translate("Form", "Directory Configuration"))
        self.RootDirectlabel.setText(_translate("Form", "Root Directory"))
        self.RootdirectBut.setText(_translate("Form", "...."))
        self.BluedirectBut.setText(_translate("Form", "...."))
        self.BlueTeamlabel.setText(_translate("Form", "Blue Team Folder"))
        self.RedTeamlabel.setText(_translate("Form", "Red Team Folder"))
        self.ReddirectBut.setText(_translate("Form", "...."))
        self.WhiteTeamLabel.setText(_translate("Form", "White Team Folder"))
        self.WhitedirectBut.setText(_translate("Form", "...."))
        self.SaveEventBut_2.setText(_translate("Form", "Start Data Ingestion"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())