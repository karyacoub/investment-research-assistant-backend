from fastapi import APIRouter

from src.services.BusinessInsightsService import BusinessInsightsService


class BusinessInsightsController:
    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route("/insights/stocks/query", self.search_ticker_keyword, methods=["GET"])
        self.router.add_api_route("/insights/stocks/{ticker}", self.get_todays_ticker_info, methods=["GET"])

        self.service = BusinessInsightsService()

    async def search_ticker_keyword(self, keyword: str | None = None):
        return self.service.get_tickers_from_keyword(keyword)

    async def get_todays_ticker_info(self, ticker: str):
        return self.service.get_ticker_info(ticker)
