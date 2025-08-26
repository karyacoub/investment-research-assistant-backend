import json

MOCK_AGENT_RESPONSE = json.dumps({
    "summary": "The latest stock price for COF (Capital One) on 2025-08-25 is $221.10, with an opening price of $221.00 and a trading volume of 1,934,434 shares. The overall sentiment for COF is 'Neutral', with a sentiment score of 0.062714. However, there are mixed signals in the news, with some articles indicating a 'Somewhat-Bullish' outlook and others suggesting a 'Neutral' stance.",
    "market_snapshot": {
    "symbol": "COF",
    "date": "2025-08-25",
    "open": 221,
    "close": 221.1,
    "volume": 1934434
    },
    "news_highlights": {
    "overall_sentiment": "Neutral",
    "sentiment_score": "0.062714",
    "top_articles": [
        {
            "title": "Is Capital One About to Create the Biggest Payment Network In America? Here's What Investors Need to Know.",
            "url": "https://www.fool.com/investing/2025/08/24/is-capital-one-about-to-create-the-biggest-payment/",
            "banner_image": "https://g.foolcdn.com/art/companylogos/square/cof.png"
        },
        {
            "title": "Why Is Capital One  ( COF )  Down 2.2% Since Last Earnings Report?",
            "url": "https://www.zacks.com/stock/news/2741010/why-is-capital-one-cof-down-22-since-last-earnings-report",
            "banner_image": "https://g.foolcdn.com/art/companylogos/square/cof.png"
        },
        {
            "title": "Here's Why Capital One  ( COF )  is a Strong Value Stock",
            "url": "https://www.zacks.com/stock/news/2740786/heres-why-capital-one-cof-is-a-strong-value-stock",
        }
    ]
    },
    "sources": [
    "market_data_tool",
    "news_sentiment_tool"
    ]
})