
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

from GUI_Subsystem.loading_screen import LoadingScreen
from GUI_Subsystem.PICK_GUI import Ui_MainWindow
from GUI_Subsystem.filter import filterPopup
from GUI_Subsystem.OpenEvent_GUI import Open_Event
from GUI_Subsystem.icons import IconConfigDialog
from Directory_Configuration import Directory_config
from Event_Configuration import Event_config
from Team_Configuration import Team_config
from Splunk.Splunk import Splunk_Class
from Data_Processing.Log_File import Log_File
from Data_Processing.Enforcement_Action_Report import Enforcement
from DBManager import DBManager
from Documentation.Vector import Vector
from Documentation.Log_Entry import Log_Entry
from Visual.Real_Time_Actualization.Graph import Graph

def retranslateUi(MainWindow):
    pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        #Central widget
        self.centWid = self.findChild(QtWidgets.QWidget,'centralwidget')
        
        #Graph Instance and necessary variables
        self.GraphViewGraphImg = self.centWid.findChild(QtWidgets.QGraphicsView, 'GraphViewGraphPlace')          #graphview Tab
        self.DoubleViewGraphImg = self.centWid.findChild(QtWidgets.QGraphicsView, 'DoubleViewGraphicsPlace')    #doubleview Tab
        self.graph = Graph(self.GraphViewGraphImg,self.DoubleViewGraphImg)

        #Declare filter popup and set buttons
        self.filters = filterPopup()
        self.filters.buttonBox.accepted.connect(self.filterEntries)
        self.filters.buttonBox.rejected.connect(self.closeFilter)

        self.openEvent = Open_Event()
        self.openEvent.buttonBox.accepted.connect(self.openListEvent)
        self.openEvent.buttonBox.rejected.connect(self.closeOpenEvent)

        #Declare config classes variables

        self.dirConfig = Directory_config()
        self.eventConfig = Event_config(self.dirConfig)
        self.teamConfig = Team_config(self.eventConfig)

        #Configure Main Buttons

        self.filtButt = self.centWid.findChild(QtWidgets.QPushButton,'LogEntryFilterBut')
        self.filtButt.clicked.connect(self.showFilter)
        self.newButt = self.findChild(QtWidgets.QAction,'actionNew')
        self.newButt.triggered.connect(self.teamConfig.showTeamConfig)
        self.openButt = self.findChild(QtWidgets.QAction,'actionOpen')
        self.openButt.triggered.connect(self.showOpenEvent)
        self.graphViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'GraphViewIconConfigBut')
        self.doubViewIconButt = self.centWid.findChild(QtWidgets.QPushButton, 'DoubleViewIconConfigBut')
        self.graphViewIconButt.clicked.connect(self.showIcons)
        self.doubViewIconButt.clicked.connect(self.showIcons)
        self.eventConfigButt = self.findChild(QtWidgets.QAction,'actionEvent_Configuration_2')
        self.eventConfigButt.triggered.connect(self.eventConfig.showEventConfig)
        self.dirConfigButt = self.findChild(QtWidgets.QAction,'actionDir_Configuration')
        self.dirConfigButt.triggered.connect(self.dirConfig.showDirectoryConfig)
        self.teamConfigButt = self.findChild(QtWidgets.QAction,'actionTeam_Configuration')
        self.teamConfigButt.triggered.connect(self.teamConfig.showTeamConfig)
        self.addVectorButt = self.centWid.findChild(QtWidgets.QPushButton,'VectorConfigAddVectorBut')
        self.addVectorButt.clicked.connect(self.addVector)

        
        #Some tables
        self.logETable = self.centWid.findChild(QtWidgets.QTableWidget,'LogEntryTable')
        self.logETable.cellChanged.connect(self.addLogtoVector)
        self.vectorTable = self.centWid.findChild(QtWidgets.QTableWidget,'VectorConfigTable')
        self.vectorTable.cellChanged.connect(self.vectorEdited)

        #Splunk INstance
        self.splunker = Splunk_Class()

        #COnnect Directory Ingestion with button here
        self.dirConfig.DirecConfig.findChild(QtWidgets.QPushButton, 'SaveEventBut').clicked.connect(self.saveAndStartIngestion)

        #Connect open button
        #self.openEvent.findChild(QtWidgets.QPushButton, "OpenEvent").clicked.connect(self.openListEvent)
        self.GraphViewAddNodeBut = self.findChild(QtWidgets.QPushButton, "GraphViewAddNodeBut")
        self.GraphViewAddNodeBut.clicked.connect(self.graph.addNewNode)
        self.GraphViewDeleteNodeBut = self.findChild(QtWidgets.QPushButton, "GraphViewDeleteNodeBut")
        self.GraphViewDeleteNodeBut.clicked.connect(self.graph.deleteNode)
        self.DoubleViewAddNodeBut = self.findChild(QtWidgets.QPushButton, "DoubleViewAddNodeBut")
        self.DoubleViewAddNodeBut.clicked.connect(self.graph.addNewNode)
        self.DoubleViewDeleteNodeBut = self.findChild(QtWidgets.QPushButton, "DoubleViewDeleteNodeBut")
        self.DoubleViewDeleteNodeBut.clicked.connect(self.graph.deleteNode)
        self.GraphViewAddRelationshipBut = self.findChild(QtWidgets.QPushButton, 'GraphViewAddRelationshipBut')
        self.GraphViewAddRelationshipBut.clicked.connect(self.graph.addRelationship)
        #EXPORT BUTTONS
        self.GraphExportPNG = self.findChild(QtWidgets.QAction, "actionPNG_2")                                  #find the export button
        self.GraphExportPNG.triggered.connect(self.graph.ExportGraphPNG)
        self.GraphExportJPEG = self.findChild(QtWidgets.QAction, "actionJPEG_2")
        self.GraphExportJPEG.triggered.connect(self.graph.ExportGraphJPEG)
        



        self.graph.createGraph(["Red attack","Blue defend","red attack 2", "blue defend 2"])

        #Initialize Data Structures
        self.vectors = [] #Empty list that will be populated with vectors
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.show()
        #self.teamConfig.showTeamConfig()

    def saveAndStartIngestion(self):
        id = DBManager.insert_directory(self.dirConfig.rootFolder ,self.dirConfig.whiteFolder, self.dirConfig.blueFolder, self.dirConfig.redFolder, self.eventConfig.id)
        self.startIngestion()
        
    def startIngestion(self):
        if(self.dirConfig.checkFolders()):
            #Display splash screen
            self.splash = LoadingScreen()
            
            self.dirConfig.DirecConfig.close()
            self.readLogFiles(self.dirConfig.whiteFolder)
            self.readLogFiles(self.dirConfig.blueFolder)
            self.readLogFiles(self.dirConfig.redFolder)
            self.validateInSplunk()
            self.splash.stopLoading()
            self.show()
            self.populateLogEntryTable()

    #Method to validate files in Splunk, it deletes files outside of the event configuration part
    def validateInSplunk(self):
        indexes = ["blue_team","red_team","white_team"]
        filters = {
            "startTime":"",
            "endTime": self.eventConfig.startDate,
            "keywords": "| delete"
        }
        self.splunker.search(indexes,filters)
        filters = {
            "startTime":self.eventConfig.endDate,
            "endTime": "+10y",
            "keywords": "| delete"
        }
        self.splunker.search(indexes,filters)
        
    def openListEvent(self):
        if(not self.openEvent.eventList.currentRow() == -1):
            self.eventConfig.id = self.openEvent.eventList.currentItem().data(Qt.UserRole)
            query = DBManager.get_single_directory(self.eventConfig.id)
            self.dirConfig.whiteFolder = query['whiteFolder']
            self.dirConfig.blueFolder = query['blueFolder']
            self.dirConfig.redFolder = query['redFolder']
            self.startIngestion()
            self.openEvent.close()

    #Method to show filter popup
    def showFilter(self):
        if(not self.eventConfig.id == 0):
            query = DBManager.get_single_event(self.eventConfig.id)
            self.filters.setDT(startDT = query['StartDate'], endDT = query['EndDate'])
        self.filters.show()
    #Method to close filter popup without doing anything
    def closeFilter(self):
        self.filters.close()

    def showOpenEvent(self):
        query = DBManager.get_multiple_events()
        self.openEvent = Open_Event(events= query)
        self.openEvent.buttonBox.accepted.connect(self.openListEvent)
        self.openEvent.buttonBox.rejected.connect(self.closeOpenEvent)
        self.openEvent.show()

    def closeOpenEvent(self):
        self.openEvent.close()

    #Method to search in splunk with filters from the filter popup
    def filterEntries(self):
        index = []
        index.append("*")
        index.append("")
        index.append("")
        keywords = str(self.filters.keyWordSearch.text())
        startTime = self.filters.startTime.dateTime().toString("yyyy-MM-ddThh:mm:ss")
        endTime = self.filters.endTime.dateTime().toString("yyyy-MM-ddThh:mm:ss")

        #Check which boxes are checked to search proper folders
        if((self.filters.blueBox.isChecked() == True or self.filters.blueBox2.isChecked() == True) and (self.filters.redBox.isChecked() == True or self.filters.redBox2.isChecked() == True) and (self.filters.whiteBox.isChecked() == True or self.filters.whiteBox2.isChecked() == True)):
            index[0] = "blue_team"
            index[1] ="red_team"
            index[2] = "white_team"
        elif((self.filters.redBox.isChecked() == True or self.filters.redBox2.isChecked() == True) and (self.filters.whiteBox.isChecked() == True or self.filters.whiteBox2.isChecked() == True)):
            index[0] = "red_team"
            index[1] ="white_team"
        elif((self.filters.blueBox.isChecked() == True or self.filters.blueBox2.isChecked() == True) and (self.filters.whiteBox.isChecked() == True or self.filters.whiteBox2.isChecked() == True)):
            index[0] = "blue_team"
            index[1] = "white_team"
        elif((self.filters.blueBox.isChecked() == True or self.filters.blueBox2.isChecked() == True) and (self.filters.redBox.isChecked() == True or self.filters.redBox2.isChecked() == True)):
            index[0] = "blue_team"
            index[1] ="red_team"
        elif(self.filters.redBox.isChecked() == True or self.filters.redBox2.isChecked() == True):
            index[0] ="red_team"
        elif(self.filters.whiteBox.isChecked() == True or self.filters.whiteBox2.isChecked() == True):
            index[0] = "white_team"
        elif(self.filters.blueBox.isChecked() == True or self.filters.blueBox2.isChecked() == True):
            index[0] = "blue_team"

        filters = {
            "startTime":startTime,
            "endTime":endTime,
            "keywords":keywords
        }
        entries = self.splunker.search(index,filters)
        self.populateEntryTable(entries)

    def showIcons(self):
        exPopup = IconConfigDialog(self)
        exPopup.show()


#Method to read files and put them into log file in the table
    def readLogFiles(self,dir):
        #We get log file table to show files with errors
        self.logFTable = self.centWid.findChild(QtWidgets.QTableWidget,'logFileTable')
        
        #We create our list of Log Files
        self.logFiles = []

        #Now we populate list of log files here
        for filename in os.listdir(dir):
            self.logFiles.append(Log_File(filename,dir))
        
        #For each log file we get we attempt to cleanse
        for file in self.logFiles:
            file.cleanseFile()
            if(not file.cleansed):
                #We send it to enforcement action report
                self.viewEnforcementReport(file)

        #We upload files that were cleansed
        #FIXME For now we just upload files in folder
        self.uploadToSplunk(dir)

        #Method that demoes the splunk behavior
    def uploadToSplunk(self,dir):
        #We check what the directory is to select proper place to upload
        if(os.path.basename(dir)=="Blue Team"):
            index = "blue_team"
        elif(os.path.basename(dir)=="Red Team"):
            index = "red_team"
        elif(os.path.basename(dir)=="White Team"):
            index = "white_team"
        #Upload files to splunk
        self.splunker.uploadFiles(dir,index)

    def searchFromSplunk(self,searchIndex):
        #Read files from splunk
        index = searchIndex
        filters = {
            "startTime":"",
            "endTime":"",
            "keywords":""
        }
        self.logEntries = self.splunker.search(index,filters)

        #Show files obtained from Splunk
        for log in self.logEntries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +" "+ log[3] +" "+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

    #Method that populates the log entry table with proper log entries for demo
    #FIXME is for demo
    def populateLogEntryTable(self):
        index = ["white_team","blue_team","red_team"]
        filters = {
            "startTime":"",
            "endTime":"",
            "keywords":""
        }
        entries = self.splunker.search(index,filters)

        #Show files obtained from Splunk
        for log in entries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +"\n"+ log[3] +"\n"+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))


    def populateEntryTable(self,entries):
        self.logETable.setRowCount(0)
        for log in entries:
            rowPosition = self.logETable.rowCount()
            self.logETable.insertRow(rowPosition)
            self.logETable.setItem(rowPosition,0,QTableWidgetItem(log[0]))
            self.logETable.setItem(rowPosition,1,QTableWidgetItem(log[2]))
            self.logETable.setItem(rowPosition,2,QTableWidgetItem(log[1] +"\n"+ log[3] +"\n"+ log[4]))
            self.logETable.setItem(rowPosition,4,QTableWidgetItem("Vector 1"))

    #Method that creates a Vector adding it to the list of vectors
    def addVector(self):
        rowPosition = self.vectorTable.rowCount()
        self.vectorTable.insertRow(rowPosition)
        self.vectors.append(Vector())

    def vectorEdited(self):
        col = self.vectorTable.currentColumn()
        row = self.vectorTable.currentRow()
        item = self.vectorTable.currentItem().text()
        if col == 1:
            self.vectors[row].setName(item)
        elif col == 2:
            self.vectors[row].setDescription(item)
        
    def deleteVector(self):
        selected = self.vectorTable.selectedItems()
        if selected:
            for item in selected:
                self.vectorTable.removeRow(item.row())
                self.vectors.pop(item.row())

    def addLogtoVector(self):
        col = self.logETable.currentColumn()
        if col != 3:
            return
        row = self.logETable.currentRow()
        item = self.logETable.currentItem().text()
        for vector in self.vectors:
            if(vector.name == item):
                vector.addLogEntry(Log_Entry(self.logETable.item(row,0),self.logETable.item(row,1),self.logETable.item(row,2)))


    # Window resizeable
    def setResizeMode(self, SizeRootObjectToView):
        pass


app = QtWidgets.QApplication(sys.argv)
x=0
window = MainWindow()
app.exec()
