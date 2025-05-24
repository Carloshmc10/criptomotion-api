import praw
from pyton.sentiment_analysis import SentimentAnalyzer
from pyton.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

class RedditFetcher:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        self.analyzer = SentimentAnalyzer()

    def fetch_and_analyze(self, subreddit="cryptocurrency", keyword="ethereum", limit=5):
        posts = self.reddit.subreddit(subreddit).search(keyword, limit=limit)
        results = []
        for post in posts:
            text = post.title + " " + (post.selftext or "")
            sentiment = self.analyzer.analyze(text)
            results.append({"text": text, "sentiment": sentiment})
        return results if results else []
