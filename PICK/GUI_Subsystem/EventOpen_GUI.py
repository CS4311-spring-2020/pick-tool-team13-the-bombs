
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout


class openEvent(QDialog):

    def __init__(self, parent=None, events= {}):
        super().__init__(parent)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.eventsSavedLabel = QLabel("Events Saved",self)
        self.resize(408, 416)

        self.openButt = QPushButton(self)
        self.openButt.setText("Open")
        self.eventList = QListWidget(self)
        #print(events)
        for event in events:
            itemN = QListWidgetItem()
            itemN.setText('Event Name: ' + event['EventName'] + '    Event Description: ' + event['EventDescription'])
            self.eventList.addItem(itemN)

        verticalLayout_2 = QVBoxLayout(self)
        verticalLayout_2.addWidget(self.eventsSavedLabel)
        self.gridLayout = QGridLayout()        
        
        self.gridLayout.addWidget(self.eventList, 0, 0, 1, 1)
        verticalLayout_2.addLayout(self.gridLayout)
        verticalLayout_2.addWidget(self.openButt)
