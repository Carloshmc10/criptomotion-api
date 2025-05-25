from pymongo import MongoClient
from config import MONGODB_URI, MONGODB_DBNAME, COLLECTION_MARKETS

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[MONGODB_DBNAME]
        self.market_collection = self.db[COLLECTION_MARKETS]
        self.reddit_collection = self.db["reddit_data"]

    def insert_market_data(self, data):
        if data:
            self.market_collection.insert_many(data)

    def insert_reddit_data(self, data):
        if data:
            self.reddit_collection.insert_many(data)

    def close_connection(self):
        self.client.close()
