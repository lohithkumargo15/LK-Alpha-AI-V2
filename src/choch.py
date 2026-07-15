"""
========================================================

File : choch.py

Purpose:
Detect Change of Character (CHoCH)

Developer : Lohith Kumar

========================================================
"""


def check_choch(candles):

    if len(candles) < 6:
        return "NONE"

    # Previous trend
    previous_high = candles[-3]["high"]
    previous_low = candles[-3]["low"]

    # Latest candle
    latest_high = candles[-1]["high"]
    latest_low = candles[-1]["low"]

    # Bullish CHoCH
    if latest_low < previous_low:
        return "BEARISH"

    # Bearish CHoCH
    if latest_high > previous_high:
        return "BULLISH"

    return "NONE"