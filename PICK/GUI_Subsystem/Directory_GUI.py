# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directory.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DirectoryConfig(object):
    def setupUi(self, DirectoryConfig):
        DirectoryConfig.setObjectName("DirectoryConfig")
        DirectoryConfig.resize(1171, 681)
        self.verticalLayout = QtWidgets.QVBoxLayout(DirectoryConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DirectoryTitle = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.DirectoryTitle.setFont(font)
        self.DirectoryTitle.setObjectName("DirectoryTitle")
        self.verticalLayout.addWidget(self.DirectoryTitle, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.RootDirectTextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        self.RootDirectTextbox.setObjectName("RootDirectTextbox")
        self.gridLayout.addWidget(self.RootDirectTextbox, 0, 1, 1, 1)
        self.RootDirectlabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RootDirectlabel.setFont(font)
        self.RootDirectlabel.setObjectName("RootDirectlabel")
        self.gridLayout.addWidget(self.RootDirectlabel, 0, 0, 1, 1)
        self.BlueTeamTextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        self.BlueTeamTextbox.setObjectName("BlueTeamTextbox")
        self.gridLayout.addWidget(self.BlueTeamTextbox, 0, 4, 1, 1)
        self.RedTeamtextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        self.RedTeamtextbox.setObjectName("RedTeamtextbox")
        self.gridLayout.addWidget(self.RedTeamtextbox, 1, 1, 1, 1)
        self.RootdirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.RootdirectBut.setObjectName("RootdirectBut")
        self.gridLayout.addWidget(self.RootdirectBut, 0, 2, 1, 1)
        self.RedTeamlabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RedTeamlabel.setFont(font)
        self.RedTeamlabel.setObjectName("RedTeamlabel")
        self.gridLayout.addWidget(self.RedTeamlabel, 1, 0, 1, 1)
        self.ReddirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.ReddirectBut.setObjectName("ReddirectBut")
        self.gridLayout.addWidget(self.ReddirectBut, 1, 2, 1, 1)
        self.BlueTeamlabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BlueTeamlabel.setFont(font)
        self.BlueTeamlabel.setObjectName("BlueTeamlabel")
        self.gridLayout.addWidget(self.BlueTeamlabel, 0, 3, 1, 1)
        self.BluedirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.BluedirectBut.setObjectName("BluedirectBut")
        self.gridLayout.addWidget(self.BluedirectBut, 0, 5, 1, 1)
        self.whiteTeamTextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        self.whiteTeamTextbox.setObjectName("whiteTeamTextbox")
        self.gridLayout.addWidget(self.whiteTeamTextbox, 1, 4, 1, 1)
        self.WhitedirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.WhitedirectBut.setObjectName("WhitedirectBut")
        self.gridLayout.addWidget(self.WhitedirectBut, 1, 5, 1, 1)
        self.WhiteTeamLabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WhiteTeamLabel.setFont(font)
        self.WhiteTeamLabel.setObjectName("WhiteTeamLabel")
        self.gridLayout.addWidget(self.WhiteTeamLabel, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.SaveEventBut = QtWidgets.QPushButton(DirectoryConfig)
        self.goBackToEvent = QtWidgets.QPushButton(DirectoryConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveEventBut.sizePolicy().hasHeightForWidth())
        self.SaveEventBut.setSizePolicy(sizePolicy)
        self.SaveEventBut.setObjectName("SaveEventBut")
        self.verticalLayout.addWidget(self.SaveEventBut)
        sizePolicy.setHeightForWidth(self.goBackToEvent.sizePolicy().hasHeightForWidth())
        self.goBackToEvent.setSizePolicy(sizePolicy)
        self.goBackToEvent.setObjectName("goBackToEvent")
        self.verticalLayout.addWidget(self.goBackToEvent)
        

        self.retranslateUi(DirectoryConfig)
        QtCore.QMetaObject.connectSlotsByName(DirectoryConfig)

    def retranslateUi(self, DirectoryConfig):
        _translate = QtCore.QCoreApplication.translate
        DirectoryConfig.setWindowTitle(_translate("DirectoryConfig", "Form"))
        self.DirectoryTitle.setText(_translate("DirectoryConfig", "Directory Configuration"))
        self.RootDirectlabel.setText(_translate("DirectoryConfig", "Root Directory"))
        self.RootdirectBut.setText(_translate("DirectoryConfig", "...."))
        self.RedTeamlabel.setText(_translate("DirectoryConfig", "Red Team Folder"))
        self.ReddirectBut.setText(_translate("DirectoryConfig", "...."))
        self.BlueTeamlabel.setText(_translate("DirectoryConfig", "Blue Team Folder"))
        self.BluedirectBut.setText(_translate("DirectoryConfig", "...."))
        self.WhitedirectBut.setText(_translate("DirectoryConfig", "...."))
        self.WhiteTeamLabel.setText(_translate("DirectoryConfig", "White Team Folder"))
        self.SaveEventBut.setText(_translate("DirectoryConfig", "Start Data Ingestion"))
        self.goBackToEvent.setText(_translate("DirectoryConfig", "Go Back to Event Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DirectoryConfig = QtWidgets.QWidget()
    ui = Ui_DirectoryConfig()
    ui.setupUi(DirectoryConfig)
    DirectoryConfig.show()
    sys.exit(app.exec_())
