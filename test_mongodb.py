from pymongo import MongoClient

uri = "mongodb+srv://satyampawar_ds:Admin1234@cluster0.vusv6qf.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    client.admin.command("ping")
    print("MongoDB connection successful")
except Exception as e:
    print("MongoDB connection failed:")
    print(e)