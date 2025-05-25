from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from sentiment_analysis import SentimentAnalyzer  # importa o analisador
from config import SUPPORTED_COINS
import requests

app = Flask(__name__)
CORS(app)

# Credencial errada
client = MongoClient("mongodb://localhost:27017")
db = client["cryptomotion"]

analyzer = SentimentAnalyzer()  # instância do analisador

coins =""
for item in SUPPORTED_COINS:
    coins += item+","


@app.route("/api/coins")
def get_all_coins():
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets",
    params= {
        "vs_currency": "brl",
        "symbols": coins})
    print(response.status_code)
    return response.json()

@app.route("/api/market")
def get_market_data():
    data = list(db["market_data"].find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/api/reddit")
def get_reddit_data():
    raw_data = list(db["reddit_data"].find({}, {"_id": 0}))
    
    enriched_data = []
    for item in raw_data:
        text = item.get("text", "")
        sentiment = analyzer.analyze(text)
        enriched_data.append({
            **item,
            "sentiment": sentiment
        })

    return jsonify(enriched_data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
