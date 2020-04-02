# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Event.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventConfig(object):
    def setupUi(self, EventConfig):
        EventConfig.setObjectName("EventConfig")
        EventConfig.resize(1171, 680)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EventConfig)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EventTitlelabel = QtWidgets.QLabel(EventConfig)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.EventTitlelabel.setFont(font)
        self.EventTitlelabel.setObjectName("EventTitlelabel")
        self.verticalLayout_2.addWidget(self.EventTitlelabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.EventConfigEndDate = QtWidgets.QDateTimeEdit(EventConfig)
        self.EventConfigEndDate.setObjectName("EventConfigEndDate")
        self.gridLayout.addWidget(self.EventConfigEndDate, 2, 3, 1, 1)
        self.DescriptionTextbox = QtWidgets.QTextEdit(EventConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionTextbox.sizePolicy().hasHeightForWidth())
        self.DescriptionTextbox.setSizePolicy(sizePolicy)
        self.DescriptionTextbox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.DescriptionTextbox.setObjectName("DescriptionTextbox")
        self.gridLayout.addWidget(self.DescriptionTextbox, 2, 1, 1, 1)
        self.EventDescriptionlabel = QtWidgets.QLabel(EventConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EventDescriptionlabel.sizePolicy().hasHeightForWidth())
        self.EventDescriptionlabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventDescriptionlabel.setFont(font)
        self.EventDescriptionlabel.setObjectName("EventDescriptionlabel")
        self.gridLayout.addWidget(self.EventDescriptionlabel, 2, 0, 1, 1)
        self.EventEndTextbox = QtWidgets.QTextEdit(EventConfig)
        self.EventEndTextbox.setMaximumSize(QtCore.QSize(1000, 200))
        self.EventEndTextbox.setObjectName("EventEndTextbox")
        self.gridLayout.addWidget(self.EventEndTextbox, 1, 1, 1, 1)
        self.EventConfigStartDate = QtWidgets.QDateTimeEdit(EventConfig)
        self.EventConfigStartDate.setObjectName("EventConfigStartDate")
        self.gridLayout.addWidget(self.EventConfigStartDate, 1, 3, 1, 1)
        self.EventStartlabel = QtWidgets.QLabel(EventConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EventStartlabel.sizePolicy().hasHeightForWidth())
        self.EventStartlabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventStartlabel.setFont(font)
        self.EventStartlabel.setObjectName("EventStartlabel")
        self.gridLayout.addWidget(self.EventStartlabel, 1, 2, 1, 1)
        self.EventEndlabel = QtWidgets.QLabel(EventConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EventEndlabel.sizePolicy().hasHeightForWidth())
        self.EventEndlabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventEndlabel.setFont(font)
        self.EventEndlabel.setObjectName("EventEndlabel")
        self.gridLayout.addWidget(self.EventEndlabel, 2, 2, 1, 1)
        self.EventNamelabel = QtWidgets.QLabel(EventConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EventNamelabel.sizePolicy().hasHeightForWidth())
        self.EventNamelabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EventNamelabel.setFont(font)
        self.EventNamelabel.setObjectName("EventNamelabel")
        self.gridLayout.addWidget(self.EventNamelabel, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.saveEventButt = QtWidgets.QPushButton(EventConfig)
        self.saveEventButt.setObjectName("saveEventButt")
        self.verticalLayout_2.addWidget(self.saveEventButt)

        self.retranslateUi(EventConfig)
        QtCore.QMetaObject.connectSlotsByName(EventConfig)

    def retranslateUi(self, EventConfig):
        _translate = QtCore.QCoreApplication.translate
        EventConfig.setWindowTitle(_translate("EventConfig", "Form"))
        self.EventTitlelabel.setText(_translate("EventConfig", "Event Configuration"))
        self.EventDescriptionlabel.setText(_translate("EventConfig", "Event Description"))
        self.EventStartlabel.setText(_translate("EventConfig", "Event Start timestamp"))
        self.EventEndlabel.setText(_translate("EventConfig", "Event End timestamp"))
        self.EventNamelabel.setText(_translate("EventConfig", "Event Name"))
        self.saveEventButt.setText(_translate("EventConfig", "Save Event"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventConfig = QtWidgets.QWidget()
    ui = Ui_EventConfig()
    ui.setupUi(EventConfig)
    EventConfig.show()
    sys.exit(app.exec_())
