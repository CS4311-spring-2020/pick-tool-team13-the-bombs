from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QGridLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class Open_Event(QDialog):

    def __init__(self, parent=None, events= {}):
    
        super().__init__(parent)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.eventsSavedLabel = QLabel("Events Saved",self)
        self.resize(408, 416)
        verticalLayout_2 = QVBoxLayout(self)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.eventList = QListWidget(self)

        for event in events:
            #print(event)
            itemN = QListWidgetItem()
            itemN.setData(Qt.UserRole, event['_id'])
            itemN.setText('Event Name: ' + event['EventName'] + '    Event Description: ' + event['EventDescription'])
            self.eventList.addItem(itemN)

        verticalLayout_2.addWidget(self.eventsSavedLabel)
        self.gridLayout = QGridLayout()        
        
        self.gridLayout.addWidget(self.eventList, 0, 0, 1, 1)
        verticalLayout_2.addLayout(self.gridLayout)
        verticalLayout_2.addWidget(self.buttonBox)