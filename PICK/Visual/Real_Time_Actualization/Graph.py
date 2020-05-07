
import sys
import os
import pydot

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import (QApplication,QWidget, QFormLayout,QCheckBox, QGroupBox, QWidget,QLineEdit,QDialogButtonBox, QLabel, QMainWindow, QAction, qApp, QPushButton, QDialog,QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle, QDialogButtonBox, QTableWidgetItem ,QSplashScreen,QGraphicsScene, QGraphicsItem, QGraphicsLineItem)
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSlot, QLineF
from IPython.display import Image, display

x=0
class Graph(object):
    def __init__(self,graphView,doubleView):
        self.scene  =QGraphicsScene() 
        self.GraphViewGraphImg = graphView          #graphview Tab
        self.DoubleViewGraphImg = doubleView    #doubleview Tab
        self.GraphViewGraphImg.setScene(self.scene)
        self.DoubleViewGraphImg.setScene(self.scene)

        # Generate Graph
    def createGraph(self, nodeList):
        for i in range(len(nodeList)): 
            self.createGraphHelper(nodeList[i])

    def createGraphHelper(self, nodeItem):
        G = pydot.Dot(graph_type="digraph")
        node = pydot.Node(nodeItem)
        G.add_node(node)
        
        _bytes = G.create(format='png')
        image = QPixmap()
        
        image.loadFromData(_bytes)
        
        node1 = self.scene.addPixmap(image)
        node1.setFlag(QGraphicsItem.ItemIsMovable)
        node1.setFlag(QGraphicsItem.ItemIsSelectable)


        im = Image(G.create_png())
        #display(im)
        
    # Add New Node to graph
    def addNewNode(self):
        global x 
        x += 1

        G = pydot.Dot(graph_type="digraph")
        node = pydot.Node("Node #" + str(x))
        G.add_node(node)
        
        _bytes = G.create(format='png')
        image = QPixmap()
        
        image.loadFromData(_bytes)
        
        node1 = self.scene.addPixmap(image)
        node1.setFlag(QGraphicsItem.ItemIsMovable)
        node1.setFlag(QGraphicsItem.ItemIsSelectable)


        im = Image(G.create_png())
        #display(im)

    # Delete Node from Graph
    def deleteNode(self):
        selectedNode = self.scene.selectedItems()
        if(len(selectedNode) == 0):
            print("Nothing selected")  
        else:
            self.scene.removeItem(selectedNode[0])
        

    # Add Relationship
    def addRelationship(self):
        selectedNode = self.scene.selectedItems()
        if(len(selectedNode) < 2):
            print("Not enough nodes selected")
        elif(len(selectedNode) > 2):
            print("Too many nodes selected")
        elif(len(selectedNode) == 2):
            print(selectedNode[0].pos(), selectedNode[1].pos())
            qitem = QGraphicsLineItem(QLineF(selectedNode[0].pos(), selectedNode[1].pos()))
            self.scene.addItem(qitem)
    
    def ExportGraphJPEG(self):
       # with open("GraphEXPORTED.png", "wb") as f:
       #     f.write(self._bytes)
       
       pixmap = self.GraphViewGraphImg.grab()
       pixmap.save("GraphEXPORTED.jpeg")
    
    def ExportGraphPNG(self):
       # with open("GraphEXPORTED.png", "wb") as f:
       #     f.write(self._bytes)
       
       pixmap = self.GraphViewGraphImg.grab()
       pixmap.save("GraphEXPORTED.png")
