import json

MOCK_AGENT_RESPONSE_COF = json.dumps({
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

MOCK_AGENT_RESPONSE_NVDA_ETF = json.dumps({
    "summary": "Nvidia's earnings could have a significant impact on semiconductor ETFs like the SOXX, as Nvidia is a major player in the semiconductor industry. The recent market data shows that Nvidia's stock closed at $181.77 on August 26, 2025, with a volume of 167,157,196 shares. The SOXX, which tracks the performance of semiconductor companies, closed at $250.85 on the same day with a volume of 3,734,686 shares. The overall sentiment for Nvidia is neutral, but there are some articles that are somewhat bullish, particularly regarding its long-term performance and market capitalization. These factors suggest that Nvidia's earnings could influence the broader semiconductor ETFs, potentially driving up their prices if the earnings are strong.",
    "market_snapshot": {
        "symbol": "NVDA",
        "date": "2025-08-26",
        "open": 180.055,
        "close": 181.77,
        "volume": 167157196
    },
    "news_highlights": {
        "overall_sentiment": "Neutral",
        "sentiment_score": "0.060763",
        "top_articles": [
            {
                "title": "Asia-Pacific markets set to open higher following Wall Street gains overnight",
                "url": "https://www.cnbc.com/2025/08/27/asia-pacific-markets-live-india-tariffs-nifty-50-nikkei-225.html",
                "banner_image": None
            },
            {
                "title": "Pony.ai eyes 'sizeable fleet' in Hong Kong, unfazed by Tesla robotaxi competition",
                "url": "https://www.scmp.com/tech/tech-trends/article/3323243/chinas-ponyai-eyes-sizeable-fleet-hong-kong-unfazed-tesla-robotaxi-competition",
                "banner_image": "https://img.i-scmp.com/cdn-cgi/image/fit=contain,width=1024,format=auto/sites/default/files/d8/images/canvas/2025/08/26/14d74517-e160-42f0-aa85-6f00d99bb1be_1126e908.jpg"
            },
            {
                "title": "Here's How Much $1000 Invested In NVIDIA 10 Years Ago Would Be Worth Today - NVIDIA  ( NASDAQ:NVDA ) ",
                "url": "https://www.benzinga.com/insights/news/25/08/47347462/heres-how-much-1000-invested-in-nvidia-10-years-ago-would-be-worth-today",
                "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png"
            }
        ]
    },
    "sources": [
        "market_data_tool",
        "news_sentiment_tool"
    ]
})

MOCK_AGENT_RESPONSE_TSLA_CHPT = json.dumps({
  "summary": "Tesla's recent earnings and market performance have had a mixed impact on Chargepoint's business. While Tesla's stock has shown some bullish sentiment in certain articles, its performance in China and overall sales trends have raised concerns. Chargepoint, on the other hand, has seen a neutral sentiment in recent news, with its stock showing modest gains. The overall market dynamics suggest that Tesla's performance could influence Chargepoint's business, particularly in the EV charging infrastructure space.",
  "market_snapshot": {
    "symbol": "TSLA",
    "date": "2025-08-26",
    "open": 344.93,
    "close": 351.67,
    "volume": 75620759
  },
  "news_highlights": {
    "overall_sentiment": "N/A",
    "sentiment_score": "N/A",
    "top_articles": [
      {
        "title": "3 Top Bargain Stocks Ready for a Bull Run",
        "url": "https://www.fool.com/investing/2025/08/23/3-top-bargain-stocks-ready-for-a-bull-run/",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F830137%2Fgettyimages-1015828796.jpg&op=resize&w=700"
      },
      {
        "title": "Electrify Expo's Return to Southern California Marks Milestone Growth for the Nation's Largest EV Festival",
        "url": "https://www.benzinga.com/pressreleases/25/06/g45952407/electrify-expos-return-to-southern-california-marks-milestone-growth-for-the-nations-largest-ev-fe",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png"
      },
      {
        "title": "EV Roundup: TSLA China Sales Keep Falling, NIO Q1 Loss Widens & More",
        "url": "https://www.zacks.com/stock/news/2490863/ev-roundup-tsla-china-sales-keep-falling-nio-q1-loss-widens-more",
        "banner_image": "https://staticx-tuner.zacks.com/images/articles/main/5e/3398.jpg"
      }
    ]
  },
  "sources": [
    "market_data_tool",
    "news_sentiment_tool"
  ]
})

mock_agent_responses = [
    MOCK_AGENT_RESPONSE_COF,
    MOCK_AGENT_RESPONSE_NVDA_ETF,
    MOCK_AGENT_RESPONSE_TSLA_CHPT
]