


class Log_File(object):
    def __init__(self,name):
        self.name = name
        self.cleansed = False
        self.validated = False
        self.acknowledged = False
        self.ingested = False

    def cleanseFile(self):


        #If successfully cleansed
        self.cleansed = True
        self.validated = True
