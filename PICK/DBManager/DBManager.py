import pymongo
from bson import ObjectId

#CONNECT TO DATABASE
connection = pymongo.MongoClient("localhost", 27017)

database = connection['database']
collection = database['collection']
event_collection = database['Events']
directory_collection = database['Log entries']

print("Database connected")

#######EVENT FUNCTIONS######
def insert_event(data):
    document = event_collection.insert_one(data)
    return document.inserted_id

def update_or_event(document_id, data):
    document = event_collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged

def get_single_event(document_id):
    data = event_collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_multiple_events():
    data = event_collection.find()
    return list(data)

def update_existing_event(document_id, data):
    document = event_collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged

def remove_event(document_id):
    document = event_collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged

#######DIRECTORY FUNCTIONS######

def insert_directory(rootFolder, whiteFolder, blueFolder, redFolder, id):
    data = {'_id': id, 'rootFolder': rootFolder, 'whiteFolder': whiteFolder, 'blueFolder': blueFolder, 'redFolder': redFolder,}
    document = directory_collection.insert_one(data)
    return document.inserted_id

def get_single_directory(document_id):
    data = directory_collection.find_one({'_id': ObjectId(document_id)})
    return data

# CLOSE DATABASE
connection.close()