import os

import requests


class BusinessInsightsService:
    # AlphaVantage API key: IWRV51J9K86IOJL2
    # Global News API docs: https://www.alphavantage.co/documentation/#intelligence
    # Stock info API docs: https://www.alphavantage.co/documentation/#time-series-data

    BASE_URL = "https://www.alphavantage.co"

    def __init__(self):
        if "ALPHA_VANTAGE_API_KEY" not in os.environ:
            os.environ.setdefault("ALPHA_VANTAGE_API_KEY", "IWRV51J9K86IOJL2")

    def get_tickers_from_keyword(self, keyword: str | None):
        if keyword is None:
            return {}

        av_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
        av_api_url = f"{self.BASE_URL}/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={av_api_key}"

        result = requests.get(av_api_url)

        return result.json()

    def get_ticker_info(self, ticker: str):
        av_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
        av_api_url = f"{self.BASE_URL}/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={av_api_key}"

        result = requests.get(av_api_url)

        return result.json()