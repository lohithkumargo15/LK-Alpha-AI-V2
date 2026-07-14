"""
========================================================

File : candle_service.py

Project : LK Alpha AI

Purpose:
Fetch 1-minute OHLCV candle data.

Today:
Returns sample candles.

Later:
Will fetch live candles from TradingView/
Broker APIs.

Developer : Lohith Kumar

========================================================
"""


def get_candles(symbol: str):

    candles = []

    price = 25200

    for i in range(25):

        candles.append(
            {
                "open": price,
                "high": price + 8,
                "low": price - 5,
                "close": price + 4,
                "volume": 100000 + (i * 5000)
            }
        )

        price += 4

    return candles