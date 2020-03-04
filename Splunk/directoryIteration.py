import os

class SplunkUploader():
    def __init__(self,dir):
        self.directory = dir

    #Function that sets a list of paths of files inside the directory so that splunk can upload the files
    def setPaths(self,dir):
        paths = []
        for filename in os.listdir(dir):
            paths.append(dir+"\\"+filename)
        self.directory = paths


