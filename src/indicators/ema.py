"""
========================================================

File : ema.py

Purpose:
Calculate EMA values from candle data.

Developer : Lohith Kumar

========================================================
"""


def calculate_ema(candles, period):

    closes = [c["close"] for c in candles]

    if len(closes) < period:
        return None

    multiplier = 2 / (period + 1)

    ema = sum(closes[:period]) / period

    for price in closes[period:]:
        ema = (price - ema) * multiplier + ema

    return round(ema, 2)


def check_ema(data):

    if data.ema_9 > data.ema_20:
        return "BULLISH"

    elif data.ema_9 < data.ema_20:
        return "BEARISH"

    return "SIDEWAYS"