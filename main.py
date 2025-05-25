from fetch import MarketFetcher
from social_fetch import RedditFetcher
from db import MongoDB
import logging
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Executa coleta e análise de dados de mercado e Reddit.")
    parser.add_argument("--subreddit", default="cryptocurrency", help="Subreddit para buscar")
    parser.add_argument("--keyword", default="ethereum", help="Palavra-chave para buscar")
    parser.add_argument("--limit", type=int, default=5, help="Número de posts a coletar")
    args = parser.parse_args()

    db = MongoDB()
    market_fetcher = MarketFetcher()
    reddit_fetcher = RedditFetcher()

    try:
        logging.info("Buscando dados de mercado...")
        market_data = market_fetcher.fetch_market_data()
        db.insert_market_data(market_data)

        logging.info("Buscando e analisando dados do Reddit...")
        reddit_data = reddit_fetcher.fetch_and_analyze(
            subreddit=args.subreddit,
            keyword=args.keyword,
            limit=args.limit
        )
        db.insert_reddit_data(reddit_data)

        logging.info("Dados inseridos com sucesso no MongoDB.")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
    finally:
        db.close_connection()

if __name__ == "__main__":
    main()
