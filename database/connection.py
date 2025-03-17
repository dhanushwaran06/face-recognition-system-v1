from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["std_info"]  # Must match MongoDB Compass
collection = db["students"]

    
def get_db():
    return db
