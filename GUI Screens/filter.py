# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:39:54 2020
Menu reference: https://www.youtube.com/watch?v=aiCr9pkE5AI
@author: Irvin
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PICK menu'
        self.left = 10  # starting position from the left of the screen to the app
        self.top = 50  # start position from the top of the screen to the app
        self.width = 640  # size
        self.height = 480  # size
        self.initUI()
        

    def initUI(self):
        # create Menu bar
        bar = self.menuBar()

        file = bar.addMenu("File")
        edit = bar.addMenu("Edit")
        view = bar.addMenu("View")

        self.viewMenuBar(view)
        self.editMenuBar(edit)
        self.fileMenuBar(file)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        btn = QPushButton("Create New Vector", self)
        btn.move(20,20)
        btn.clicked.connect(self.makeVectorPopup)
        
        btn2 = QPushButton("Filter", self)
        btn2.move(20,60)
        btn2.clicked.connect(self.makeFilterPopup)
        
        
        

        self.show()

    # BUTONS IN MENU BAR
    def viewMenuBar(self, view):
        viewVecAct = QAction("View Vector", self)
        viewTabAct = QAction("View Table", self)

        view.addAction(viewVecAct)
        view.addAction(viewTabAct)

    def editMenuBar(self, edit):
        undoAct = QAction("Undo", self)
        undoAct.setShortcut('Ctrl+Z')

        redoAct = QAction("Redo", self)
        redoAct.setShortcut('Ctrl+Y')

        edit.addAction(undoAct)
        edit.addAction(redoAct)

    def fileMenuBar(self, file):
        # create actions
        saveAct = QAction("Save", self)
        saveAct.setShortcut('Ctrl+S')

        newAct = QAction("New Event", self)
        newAct.setShortcut("Ctr+N")

        quitAct = QAction("Exit", self)
        quitAct.setShortcut("Ctrl+Q")

        getJPEG = QAction("JPEG", self)
        getPNG = QAction("PNG", self)

        # exportAct = QAction("Export",self)
        file.addAction(newAct)
        file.addAction(saveAct)

        # put export, that will also contain options Like a menu whithin a menu
        exportTypes = file.addMenu("Export")
        exportTypes.addAction(getJPEG)
        exportTypes.addAction(getPNG)

        file.addAction(quitAct)

        # call Event
        quitAct.triggered.connect(self.quitEvent)

    # Events from some Buttons from Menu Bar
    def quitEvent(self):
        qApp.quit()
        
        
       
    #Make PopUp window for when user selects Filter option
    @pyqtSlot()
    def makeFilterPopup(self):
        exPopup = filterPopup(self)
        exPopup.show()
    
    
    
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
        self.startTime = QLineEdit(self)  #Start time text
        self.endTime = QLineEdit(self)    #End Time text
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

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
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.text(), self.second.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())