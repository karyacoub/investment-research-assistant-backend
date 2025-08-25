from langchain.chains import LLMChain
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

from src.services.BusinessInsightsService import BusinessInsightsService
from src.models.LLMModels import LLMPrompt

class LLMAgentService:

    def __init__(self):
        model = ChatOllama(
            model="qwen3:8b",
            reasoning=False,
            validate_model_on_init=True,
            temperature=0 # Model doesn't need to be creative in this case
        )

        tools = [
            BusinessInsightsService.get_market_data,
            BusinessInsightsService.get_news_by_ticker
        ]

        self.graph = create_react_agent(model, tools)

    async def submit_prompt(self, prompt: LLMPrompt):
        messages = {
            "messages": [
                {
                    "role": "system",
                    "content": """
                        You are an AI Investment Research Assistant for financial analysts.
                        Your job is to answer long-form financial queries by combining live market data,
                        recent financial news, and your reasoning abilities.

                        You have access to the following tools:
                        - MarketDataTool: get current stock/ETF prices and basic indicators (open, close, volume, daily change).
                        - NewsSentimentTool: retrieve recent headlines and summaries about a company.

                        When responding:
                        1. Parse the user’s query to identify relevant companies, tickers, sectors, or ETFs.
                        2. Call the MarketDataTool and/or NewsTool as needed to gather facts.
                        3. Use the retrieved data to ground your reasoning.
                        4. Always provide your final response as a JSON object in the following format:

                        ---
                        {
                            "summary": 'A string respresenting a high level answer to the user's question.'
                            "market_snapshot": {
                                "symbol": 'A string representing the ticker symbol, e.g. NVDA or AAPL.',
                                "date": 'A string representing the date of the latest stock price retireved, formatted as YYYY-mm-dd.',
                                "open": 'A double representing the opening stock price.',
                                "close": 'A double representing the closing stock price.',
                                "volume": 'An integer representing the purchase volume of stock on retireved date.'
                            }
                            "news_highlights": {
                                "overall_sentiment": 'A string representing the overall sentiment of the company.',
                                "sentiment_score": 'A string representing the score of the sentiment on a scale from 0 - 1.',
                                "top_articles": [
                                    {
                                        "title": 'A string representing the article headline.'
                                        "url": 'A string representing the article URL.'
                                    },
                                    ...
                                ]
                            }
                            "sources": ['A list of strings representing the tools that were used to generate response'.]
                        }
                        ---

                        Rules:
                        - Never make up data. If a tool does not return results, say so clearly.
                        - Be concise and professional, as if writing a research brief for an analyst.
                        - Prefer structured, skimmable output (tables, bullet points).
                    """
                },
                {
                    "role": "user",
                    "content": prompt.prompt
                }
            ]
        }

        try:
            # TODO: Any additional error handling here?
            agent_response = await self.graph.ainvoke(messages)
            return agent_response.get("messages")[-1].content
        except Exception as e:
            return f"Agent call failed: {str(e)}"
