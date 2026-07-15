"""
========================================================

File : fvg.py

Purpose:
Detect Fair Value Gap (FVG)

Developer : Lohith Kumar

========================================================
"""


def check_fvg(candles):

    if len(candles) < 3:
        return "NONE"

    candle1 = candles[-3]
    candle2 = candles[-2]
    candle3 = candles[-1]

    # Bullish FVG
    if candle1["high"] < candle3["low"]:
        return "BULLISH"

    # Bearish FVG
    if candle1["low"] > candle3["high"]:
        return "BEARISH"

    return "NONE"