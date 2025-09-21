from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
 
uri = "mongodb://localhost:27017" #mongoDB URI here
client = MongoClient(uri)
 
db = client.edu