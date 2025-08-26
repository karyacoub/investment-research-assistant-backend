import os
import requests
from langchain.tools import tool

class BusinessInsightsService:
    # TODO: remove this
    # AlphaVantage API key: IWRV51J9K86IOJL2

    def __init__(self):
        if "ALPHA_VANTAGE_API_KEY" not in os.environ:
            os.environ.setdefault("ALPHA_VANTAGE_API_KEY", "IWRV51J9K86IOJL2") # TODO: Store this in env var

    @staticmethod
    @tool("market_data_tool")
    def get_market_data(symbol: str):
        """
        Fetch the latest stock price and volume for a given ticker symbol.
        Useful when you need recent market data about a stock or ETF.

        Input:
            symbol (str): The stock ticker symbol, e.g., 'AAPL' for Apple, 'NVDA' for Nvidia.
        Output:
            A summary of the most recent trading day (open, close, volume).
        """

        av_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')

        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={av_api_key}"
        response = requests.get(url)
        data = response.json()

        if "Time Series (Daily)" not in data:
            return f"No data available for {symbol}. Response: {data}"

        latest_date = next(iter(data["Time Series (Daily)"])) # TODO: Should make sure this is sorted so it's guarenteed to get the latest date
        latest_data = data["Time Series (Daily)"][latest_date]

        return {
            "symbol": symbol,
            "data": latest_date,
            "open": latest_data['1. open'],
            "close": latest_data['4. close'],
            "volume": latest_data['5. volume']
        }

    @staticmethod
    @tool("news_sentiment_tool")
    def get_news_by_ticker(tickers: str):
        """
        Fetch recent news articles and sentiment analysis for given tickers.
        Useful for you to provide more information on a certain set of tickers, and to answer
        quetions that are more nebulous and require more information than just market data.

        Input:
            tickers (str): Comma-separated tickers (e.g., 'NVDA,AAPL').
        Output:
            Summary of sentiment and top 3 articles with headlines and URLs.
        """

        # tickers_cleaned = ",".join([tickers.strip().upper() for t in tickers.split(",")]) # In case LLM malforms input

        av_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={tickers}&apikey={av_api_key}"

        response = requests.get(url)
        data = response.json()

        if "feed" not in data or len(data["feed"]) == 0:
            return f"No news found for {tickers}"

        sentiment_label = data.get("overall_sentiment_label", "N/A")
        sentiment_score = data.get("overall_sentiment_score", "N/A")

        top_articles = data["feed"][:3]

        return {
            "overall_sentiment": sentiment_label,
            "sentiment_score": sentiment_score,
            "top_articles": top_articles
        }