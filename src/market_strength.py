"""
========================================================

File : market_strength.py

Purpose:
Measure overall market strength.

Developer : Lohith Kumar

========================================================
"""


def calculate_market_strength(score):

    bullish = score["bullish"]
    bearish = score["bearish"]

    if bullish >= 80:
        return "VERY STRONG BULLISH"

    if bullish >= 60:
        return "STRONG BULLISH"

    if bearish >= 80:
        return "VERY STRONG BEARISH"

    if bearish >= 60:
        return "STRONG BEARISH"

    return "SIDEWAYS"