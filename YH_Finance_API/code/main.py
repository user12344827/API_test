import requests
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

x_api_key=os.getenv("X-API-KEY")

# tickers = ["AAPL", "TSLA", "MSFT"]
def get_symbols_info(tickers) -> dict:
    url = "https://yfapi.net/v8/finance/chart/"
    results = {}
    for ticker in tickers: # 獲得資料
        new_url = url + ticker
        querystring = {"interval": "1d", "range": "5d"}
        headers = {"x-api-key": x_api_key}
        response = requests.request("GET", new_url, headers=headers, params=querystring)
        data = response.json()
        # print(data)

        # 轉換時間單位
        chart_data = data["chart"]["result"][0]
        timestamps = chart_data.get("timestamp", [])
        timestamps = [
            datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d")
            for timestamp in timestamps
            ]

        quote_data = chart_data["indicators"]["quote"][0]
        open_price = quote_data.get("open", [])
        close_price = quote_data.get("close", [])
        high_price = quote_data.get("high", [])
        low_price = quote_data.get("low", [])

        symbol_info_mapping = {
            timestamps[i]: {
                "open": int(open_price[i]),
                "close": int(close_price[i]),
                "high": int(high_price[i]),
                "low": int(low_price[i])
            }
            for i in range(len(timestamps))
        }

        results[ticker] = symbol_info_mapping

    return results


if __name__ == "__main__":
    tickers = ["AAPL", "TSLA", "MSFT"]
    print(get_symbols_info(tickers))