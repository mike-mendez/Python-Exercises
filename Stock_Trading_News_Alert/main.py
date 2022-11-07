from datetime import datetime, timedelta
from os import environ
from requests import get
from twilio.rest import Client

# -------------------------------- CONSTANTS ------------------------------------ #
AV_API_KEY = "[YOUR_AV_API_KEY]"
NEWS_API_KEY = "[YOUR_NEWS_API_KEY]"
STOCK_SYMBOL = "[STOCK_SYMBOL]"
COMPANY_NAME = "[COMPANY_NAME]"
TWILIO_NUM = "[YOUR_TWILIO_NUM]"
RECEIVING_NUM = "[YOUR_RECEIVING_NUM]"

# ------------------------------- TWILIO DATA ---------------------------------- #
account_sid = environ['TWILIO_ACCOUNT_SID'] = "[YOUR_TWILIO_ACCOUNT_SID]"
auth_token = environ['TWILIO_AUTH_TOKEN'] = "[YOUR_TWILIO_AUTH_TOKEN]"
client = Client(account_sid, auth_token)

# -------------------------- GETTING STOCK DATA -------------------------------- #
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_SYMBOL,
    "apikey": AV_API_KEY,
}

stock_url = f"https://www.alphavantage.co/query"
stock_r = get(stock_url, params=stock_params)
stock_data = stock_r.json()

today = datetime.today()
yesterday = (today - timedelta(1)).date() if today.weekday() != 0 else (today - timedelta(3)).date()
day_b4_yest = (today - timedelta(2)).date() if today.weekday() != 0 else (today - timedelta(4)).date()

last_close = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
second_close = float(stock_data["Time Series (Daily)"][str(day_b4_yest)]["4. close"])
pct_diff: float = round((last_close - second_close) / second_close * 100, 2)


# -------------------------- GETTING NEWS DATA --------------------------------- #
def news_alert():
    news_params = {
        "q": f'"{COMPANY_NAME}"',
        "searchIn": "title",
        "pageSize": 3,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }

    news_url = "https://newsapi.org/v2/everything"
    news_r = get(news_url, news_params)
    news_data = news_r.json()
    articles = news_data["articles"]

    # -------------------------- SENDING DATA VIA SMS ------------------------------ #
    for article in articles:
        pct_diff_msg = f"▲{pct_diff}" if pct_diff > 0 else f"▼{pct_diff}"
        body_msg = f"{STOCK_SYMBOL}: {pct_diff_msg}\n\n" \
                   f"Headline: {article['title']}\n\n" \
                   f"Brief: {article['description']}\n\n" \
                   f"URL: {article['url']}"
        message = client.messages \
            .create(
            body=body_msg,
            from_=TWILIO_NUM,
            to=RECEIVING_NUM,
        )
        print(message.status)


news_alert() if pct_diff <= -5 or pct_diff >= 5 else None
