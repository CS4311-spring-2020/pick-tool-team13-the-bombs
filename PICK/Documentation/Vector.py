from Documentation.Log_Entry import Log_Entry

class Vector(object):
    def __init__(self):
        self.logEntries = []
        self.name = ""
        self.description = ""

    def addLogEntry(self,logEntry):
        self.logEntries.append(logEntry)

    def removeLogEntry(self,logEntry):
        self.logEntries.remove(logEntry)

    def setName(self,name):
        self.name = name

    def setDescription(self,description):
        self.description = description