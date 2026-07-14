"""
========================================================

File : vwap.py

Purpose:
Calculate VWAP from candle data.

Developer : Lohith Kumar

========================================================
"""


def calculate_vwap(candles):

    total_price_volume = 0
    total_volume = 0

    for candle in candles:

        typical_price = (
            candle["high"] +
            candle["low"] +
            candle["close"]
        ) / 3

        total_price_volume += (
            typical_price *
            candle["volume"]
        )

        total_volume += candle["volume"]

    if total_volume == 0:
        return 0

    return round(
        total_price_volume / total_volume,
        2
    )


def check_vwap(data):

    if data.ltp > data.vwap:
        return "BULLISH"

    elif data.ltp < data.vwap:
        return "BEARISH"

    return "SIDEWAYS"