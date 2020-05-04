import os
import sys
import getpass
sys.path.append('splunk-sdk-python-1.6.4')
import splunklib.client as client 
import splunklib.results as results
from datetime import datetime


class Splunk_Class():
    def __init__(self):
        HOST = 'localhost'
        PORT = 8089
        USERNAME = 'admin' #Change to your own USERNAME
        PASSWORD = '' #Change to your own PASSWORD
        self.service = client.connect(host=HOST,port=PORT,username=USERNAME,password=PASSWORD)


    #Function that uploads files from a folder to splunk
    def uploadFiles(self,dir,folderType):
        paths = []
        for filename in os.listdir(dir):
            paths.append(dir+"/"+filename)
        directory = paths

        for path in directory:
            #Now Upload files to splunk one by one
            # Retrieve the index for the data
            myindex = self.service.indexes[folderType]
            # Create a variable with the path and filename
            uploadme = path
            # Upload and index the file
            myindex.upload(uploadme)

    def search(self,folderType,filters):
        #We need to check if filters are all provided so as to provide the proper search query
        if(filters['startTime'] == ""):
            #Starting time is empty so we provide earliest possible time in Zulu Time
            filters['startTime'] = "1971-01-01T00:00:00"
        elif(filters['endTime'] == ""):
            #end time is empty so we provide current time
            filters['endTime'] = datetime.utcnow().strftime("%FT%T")
        elif(filters['startTime'] == "" and filters['endTime'] == ""):
            #Starting time is empty so we provide earliest possible time in Zulu Time
            filters['startTime'] = "1971-01-01T00:00:00"
            #end time is empty so we provide current time
            filters['endTime'] = datetime.utcnow().strftime("%FT%T")

        # Run a one-shot search and display the results using the results reader
        # Set the parameters for the search:
        # - Search everything in a 24-hour time range starting June 19, 12:00pm
        # - Display the first 10 results
        kwargs_oneshot = {"starttime": "\""+filters['startTime']+"\"",
                        "endtime": "\""+filters['endTime']+"\""}
        #Search query gets all elements in Splunk
        searchquery_oneshot = "search * index=\""+folderType[0]+ "\"" + " OR index=\""+folderType[1]+"\"" + " OR index=\""+folderType[2]+"\" " +"timeformat=%F%T " + filters['keywords'] 
        print(searchquery_oneshot)
        #Perform a search
        oneshotsearch_results = self.service.jobs.oneshot(searchquery_oneshot,latest_time=filters['endTime'],earliest_time=filters['startTime'])
        # Get the results and display them using the ResultsReader
        reader = results.ResultsReader(oneshotsearch_results)

        #Data Structure that will hold the information we will show in the program from log entries
        log_entries = []

        #We will get certain data from each result of the log entries in the splunk search
        for item in reader:
            if "deleted" in item:
                print("Deleted Items")
            else:
                log_entries.append([item['_serial'],item['_raw'],item['_time'],item['source'],item['index']])

        return log_entries

# splunk = SplunkUploader()
# splunk.uploadFiles("C:\\Users\\vcone\\Desktop\\Cosas\\CS\\Software2\\GUI test\\pick-tool-team13-the-bombs\\Root\\Red Team","red_team")

# filters ={
#     "startTime":"",
#     "endTime":"2020-03-31 22:00:00",
#     "keywords":""
# }
# print(splunk.search("red_team",filters))
