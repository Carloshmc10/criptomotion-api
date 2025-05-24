from textblob import TextBlob
import re

class SentimentAnalyzer:
    def analyze(self, text):
        cleaned = self.clean_text(text)
        blob = TextBlob(cleaned)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        sentiment = self.classify_sentiment(polarity)
        return {
            'polarity': polarity,
            'subjectivity': subjectivity,
            'sentiment': sentiment
        }

    def clean_text(self, text):
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"[^\w\s]", "", text)  # Remove pontuação
        text = re.sub(r"\s+", " ", text)  # Remove espaços extras
        return text.strip()

    def classify_sentiment(self, polarity):
        if polarity >= 0.2:
            return "positive"
        elif polarity <= -0.2:
            return "negative"
        else:
            return "neutral"
