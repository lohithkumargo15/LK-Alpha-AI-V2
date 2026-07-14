"""
========================================================

File : atr.py

Purpose:
Calculate Average True Range (ATR)

Developer : Lohith Kumar

========================================================
"""


def calculate_atr(candles, period=14):

    if len(candles) < period + 1:
        return None

    true_ranges = []

    for i in range(1, len(candles)):

        current = candles[i]
        previous = candles[i - 1]

        tr = max(
            current["high"] - current["low"],
            abs(current["high"] - previous["close"]),
            abs(current["low"] - previous["close"])
        )

        true_ranges.append(tr)

    atr = sum(true_ranges[-period:]) / period

    return round(atr, 2)