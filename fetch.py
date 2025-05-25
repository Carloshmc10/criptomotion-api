import requests
import logging
from config import COINGECKO_URL

class MarketFetcher:
    def fetch_market_data(self):
        logging.info("Solicitando dados do CoinGecko...")
        response = requests.get(f"{COINGECKO_URL}/coins/markets", params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': False
        })
        if response.status_code == 200:
            logging.info("Dados de mercado obtidos com sucesso.")
            return response.json()
        else:
            logging.error(f"Falha ao buscar dados de mercado: {response.status_code}")
            raise Exception("Failed to fetch market data.")