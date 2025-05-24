import os
from dotenv import load_dotenv

load_dotenv()

# CoinGecko
COINGECKO_URL = os.getenv("COINGECKO_URL", "https://api.coingecko.com/api/v3")

# MongoDB
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DBNAME = os.getenv("DB_NAME", "cryptomotion")
COLLECTION_MARKETS = os.getenv("COLLECTION_MARKETS", "market_data")

# Reddit
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
