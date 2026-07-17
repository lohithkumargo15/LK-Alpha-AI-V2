"""
========================================================

File : order_block.py

Purpose:
Detect Bullish / Bearish Order Block

Developer : Lohith Kumar

========================================================
"""


def check_order_block(candles):

    if len(candles) < 2:
        return "NONE"

    previous = candles[-2]
    latest = candles[-1]

    # Bullish Order Block
    if (
        previous["close"] < previous["open"]
        and latest["close"] > latest["open"]
        and latest["close"] > previous["high"]
    ):
        return "BULLISH"

    # Bearish Order Block
    if (
        previous["close"] > previous["open"]
        and latest["close"] < latest["open"]
        and latest["close"] < previous["low"]
    ):
        return "BEARISH"

    return "NONE"