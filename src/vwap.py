"""
========================================================

File : vwap.py

Purpose:
Calculate VWAP and determine trend.

Developer : Lohith Kumar

========================================================
"""


def calculate_vwap(candles):
    """
    Calculate VWAP from candle data.
    """

    total_pv = 0
    total_volume = 0

    for candle in candles:

        typical_price = (
            candle["high"] +
            candle["low"] +
            candle["close"]
        ) / 3

        total_pv += typical_price * candle["volume"]
        total_volume += candle["volume"]

    # Yahoo Finance returns 0 volume for NIFTY index.
    # Prevent division by zero.
    if total_volume == 0:
        return 0.0

    return round(total_pv / total_volume, 2)


def check_vwap(ltp, vwap):
    """
    Compare LTP with VWAP.
    """

    # If VWAP is 0 (no valid volume), don't use it.
    if vwap == 0:
        return "SIDEWAYS"

    if ltp > vwap:
        return "BULLISH"

    elif ltp < vwap:
        return "BEARISH"

    return "SIDEWAYS"