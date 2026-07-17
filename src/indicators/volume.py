"""
========================================================

File : volume.py

Purpose:
Analyze market volume.

Developer : Lohith Kumar

========================================================
"""


def check_volume(candles):

    if len(candles) < 20:
        return "NORMAL"

    latest_volume = candles[-1]["volume"]

    previous_volumes = [
        candle["volume"]
        for candle in candles[-21:-1]
    ]

    average_volume = sum(previous_volumes) / len(previous_volumes)

    # Strong Volume
    if latest_volume > average_volume * 1.5:
        return "BULLISH"

    # Weak Volume
    elif latest_volume < average_volume * 0.5:
        return "BEARISH"

    return "NORMAL"