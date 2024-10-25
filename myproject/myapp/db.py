# myapp/mongo_client.py
from pymongo import MongoClient

# Replace 'localhost' and '27017' with your MongoDB server's address and port if necessary
client = MongoClient('localhost', 27017)
db = client.mydatabasedjango  # Replace with your MongoDB database name
