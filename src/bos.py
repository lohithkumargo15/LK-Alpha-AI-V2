"""
========================================================

File : bos.py

Purpose:
Detect Break of Structure (BOS)

Developer : Lohith Kumar

========================================================
"""


def check_bos(candles):

    if len(candles) < 5:
        return "NONE"

    previous_high = candles[-2]["high"]

    latest_high = candles[-1]["high"]

    previous_low = candles[-2]["low"]

    latest_low = candles[-1]["low"]

    if latest_high > previous_high:
        return "BULLISH"

    if latest_low < previous_low:
        return "BEARISH"

    return "NONE"