from pymongo import MongoClient
from pprint import pprint

# Conecta ao MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["cryptomotion"]

# Mostra amostras
print("📊 Market Data:")
for doc in db["market_data"].find().limit(3):
    pprint(doc)

print("\n📢 Reddit Data:")
for doc in db["reddit_data"].find().limit(3):
    pprint(doc)

client.close()
