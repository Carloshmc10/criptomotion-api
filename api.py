from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from sentiment_analysis import SentimentAnalyzer  # importa o analisador

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017")
db = client["cryptomotion"]

analyzer = SentimentAnalyzer()  # instância do analisador

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
