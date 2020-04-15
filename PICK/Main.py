import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem,QGraphicsScene, QGraphicsItem)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from GUI_Subsystem.PICK_GUI import Ui_MainWindow
from GUI_Subsystem.filter import filterPopup
from GUI_Subsystem.icons import IconConfigDialog
from Directory_Configuration import Directory_config
from Event_Configuration import Event_config
from Team_Configuration import Team_config

import pydot
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        #Declare config classes variables
        self.eventConfig = Event_config()
        self.dirConfig = Directory_config()
        self.teamConfig = Team_config()

        #Configure Main Buttons
        self.centWid = self.findChild(QtWidgets.QWidget,'centralwidget')
        self.filtButt = self.centWid.findChild(QtWidgets.QPushButton,'LogEntryFilterBut')
        self.filtButt.clicked.connect(self.showFilter)
        self.graphViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'GraphViewIconConfigBut')
        self.doubViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'DoubleViewIconConfigBut')
        self.graphViewIconButt.clicked.connect(self.showIcons)
        self.doubViewIconButt.clicked.connect(self.showIcons)
        self.eventConfigButt = self.findChild(QtWidgets.QAction,'actionEvent_Configuration_2')
        self.eventConfigButt.triggered.connect(self.eventConfig.showEventConfig)
        self.CreatingGraph()
        
        #Initialize Views
        self.teamConfig.showTeamConfig()

    #Method to show filter popup
    def showFilter(self):
        exPopup = filterPopup(self)
        exPopup.show()

    def showIcons(self):
        exPopup = IconConfigDialog(self)
        exPopup.show()


####################################################################################### FINALLY GRAPH
    def CreatingGraph(self):
        self.GraphViewGraphImg = self.centWid.findChild(QtWidgets.QGraphicsView, 'GraphViewGraphPlace')
        self.DoubleViewGraphImg = self.centWid.findChild(QtWidgets.QGraphicsView, 'DoubleViewGraphicsPlace')
        
        self.scene  =QGraphicsScene()
        
        self.GraphViewGraphImg.setScene(self.scene)
        self.DoubleViewGraphImg.setScene(self.scene)
        
        
        G = pydot.Dot(graph_type="digraph")
        node = pydot.Node("Hello")
        G.add_node(node)
        
        _bytes = G.create(format='png')
        image = QPixmap()
        
        image.loadFromData(_bytes)
        
        node1 = self.scene.addPixmap(image)
        node1.setFlag(QGraphicsItem.ItemIsMovable)
        
        from IPython.display import Image, display

        im = Image(G.create_png())
        display(im)
        
        
#        G = pydot.Dot(graph_type="digraph")
#        node = pydot.Node("Hello")
#        G.add_node(node)
#        _bytes = G.create(format='png')
#        image = QPixmap()
#        
#        image.loadFromData(_bytes)
        
        #self.GraphImg.setPixmap(image)
        





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()