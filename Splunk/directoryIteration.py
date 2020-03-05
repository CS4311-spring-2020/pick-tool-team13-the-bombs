import os
import sys
import getpass
sys.path.append('splunk-sdk-python-1.6.4')
import splunklib.client as client 
import splunklib.results as results


class SplunkUploader():
    def __init__(self):
        HOST = 'localhost'
        PORT = 8089
        USERNAME = 'victorvargas'
        PASSWORD = 'Isusko13-25-04'
        self.service = client.connect(host=HOST,port=PORT,username=USERNAME,password=PASSWORD)


    #Function that uploads files from a folder to splunk
    def uploadFiles(self,dir,folderType):
        paths = []
        for filename in os.listdir(dir):
            paths.append(dir+"\\"+filename)
        directory = paths

        for path in directory:
            #Now Upload files to splunk one by one
            # Retrieve the index for the data
            myindex = self.service.indexes[folderType]
            # Create a variable with the path and filename
            uploadme = path
            # Upload and index the file
            myindex.upload(uploadme)

    def readEntries(self,folderType):
        # Run a one-shot search and display the results using the results reader
        # Set the parameters for the search:
        # - Search everything in a 24-hour time range starting June 19, 12:00pm
        # - Display the first 10 results
        kwargs_oneshot = {"earliest_time": "2020-03-02T12:00:00.000-07:00",
                        "latest_time": "2020-03-04T12:00:00.000-07:00"}
        #Search query gets all elements in Splunk
        searchquery_oneshot = "search * | head 1"
        #Perform a search
        oneshotsearch_results = self.service.jobs.oneshot(searchquery_oneshot)
        # Get the results and display them using the ResultsReader
        reader = results.ResultsReader(oneshotsearch_results)

        #Data Structure that will hold the information we will show in the program from log entries
        log_entries = []

        #We will get certain data from each result of the log entries in the splunk search
        for item in reader:
            log_entries.append([item['_serial'],item['_raw'],item['_time'],item['source']])

        return log_entries
