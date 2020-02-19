# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Event.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 680)
        self.EventTitlelabel = QtWidgets.QLabel(Form)
        self.EventTitlelabel.setGeometry(QtCore.QRect(390, 20, 421, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.EventTitlelabel.setFont(font)
        self.EventTitlelabel.setObjectName("EventTitlelabel")
        self.NameTextbox = QtWidgets.QTextBrowser(Form)
        self.NameTextbox.setGeometry(QtCore.QRect(210, 130, 241, 111))
        self.NameTextbox.setObjectName("NameTextbox")
        self.EventNamelabel = QtWidgets.QLabel(Form)
        self.EventNamelabel.setGeometry(QtCore.QRect(40, 150, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventNamelabel.setFont(font)
        self.EventNamelabel.setObjectName("EventNamelabel")
        self.EventStartTextbox = QtWidgets.QTextBrowser(Form)
        self.EventStartTextbox.setGeometry(QtCore.QRect(840, 130, 241, 111))
        self.EventStartTextbox.setObjectName("EventStartTextbox")
        self.EventStartlabel = QtWidgets.QLabel(Form)
        self.EventStartlabel.setGeometry(QtCore.QRect(580, 170, 226, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventStartlabel.setFont(font)
        self.EventStartlabel.setObjectName("EventStartlabel")
        self.DescriptionTextbox = QtWidgets.QTextBrowser(Form)
        self.DescriptionTextbox.setGeometry(QtCore.QRect(210, 390, 241, 111))
        self.DescriptionTextbox.setObjectName("DescriptionTextbox")
        self.EventDescriptionlabel = QtWidgets.QLabel(Form)
        self.EventDescriptionlabel.setGeometry(QtCore.QRect(30, 420, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventDescriptionlabel.setFont(font)
        self.EventDescriptionlabel.setObjectName("EventDescriptionlabel")
        self.EventEndTextbox = QtWidgets.QTextBrowser(Form)
        self.EventEndTextbox.setGeometry(QtCore.QRect(840, 400, 241, 111))
        self.EventEndTextbox.setObjectName("EventEndTextbox")
        self.EventEndlabel = QtWidgets.QLabel(Form)
        self.EventEndlabel.setGeometry(QtCore.QRect(580, 440, 216, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventEndlabel.setFont(font)
        self.EventEndlabel.setObjectName("EventEndlabel")
        self.SaveEventBut = QtWidgets.QPushButton(Form)
        self.SaveEventBut.setGeometry(QtCore.QRect(650, 570, 483, 28))
        self.SaveEventBut.setObjectName("SaveEventBut")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.EventTitlelabel.setText(_translate("Form", "Event Configuration"))
        self.EventNamelabel.setText(_translate("Form", "Event Name"))
        self.EventStartlabel.setText(_translate("Form", "Event Start timestamp"))
        self.EventDescriptionlabel.setText(_translate("Form", "Event Description"))
        self.EventEndlabel.setText(_translate("Form", "Event End timestamp"))
        self.SaveEventBut.setText(_translate("Form", "Save Event"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    