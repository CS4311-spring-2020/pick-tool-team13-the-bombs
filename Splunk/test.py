import sys
import getpass
sys.path.append('splunk-sdk-python-1.6.4')
import splunklib.client as client
 
def setServer():
	HOST = 'localhost'
	PORT = 8089
	USERNAME = 'victorvargas'
	PASSWORD = 'Isusko13-25-04'
	service = client.connect(host=HOST,port=PORT,username=USERNAME,password=PASSWORD)

	
	# Retrieve the index for the data
	myindex = service.indexes["main"]

	# Create a variable with the path and filename
	uploadme = "C:\\Users\\vcone\\Desktop\\Cosas\\CS\\Software2\\GUI test\\pick-tool-team13-the-bombs\\Files for Testing\\Blue Team\\test2.txt"

	# Upload and index the file
	myindex.upload(uploadme)

	# Get the collection of indexes
	indexes = service.indexes

	# List the indexes and their event counts
	for index in indexes:
		count = index["totalEventCount"]
		print ("%s (events: %s)" % (index.name, count))

if __name__ == "__main__":
	setServer()