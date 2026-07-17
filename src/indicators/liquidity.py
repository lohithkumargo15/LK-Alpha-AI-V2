"""
========================================================

File : liquidity.py

Purpose:
Detect Liquidity Sweep

Developer : Lohith Kumar

========================================================
"""


def check_liquidity(candles):

    if len(candles) < 3:
        return "NONE"

    previous = candles[-2]
    latest = candles[-1]

    # Bearish Liquidity Sweep
    if (
        latest["high"] > previous["high"]
        and latest["close"] < previous["high"]
    ):
        return "BEARISH"

    # Bullish Liquidity Sweep
    if (
        latest["low"] < previous["low"]
        and latest["close"] > previous["low"]
    ):
        return "BULLISH"

    return "NONE"