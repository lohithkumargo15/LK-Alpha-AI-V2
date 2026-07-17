"""
========================================================

File : health_engine.py

Purpose:
Provides AI Health Summary.

Developer : Lohith Kumar

========================================================
"""


def get_health(data):

    bullish = 0
    bearish = 0

    indicators = [
        data.bos,
        data.choch,
        data.fvg,
        data.order_block,
        data.liquidity,
        data.volume_signal
    ]

    for indicator in indicators:

        if indicator == "BULLISH":
            bullish += 1

        elif indicator == "BEARISH":
            bearish += 1

    if bullish > bearish:

        return {
            "status": "Bullish Market",
            "bullish_indicators": bullish,
            "bearish_indicators": bearish
        }

    elif bearish > bullish:

        return {
            "status": "Bearish Market",
            "bullish_indicators": bullish,
            "bearish_indicators": bearish
        }

    return {
        "status": "Neutral Market",
        "bullish_indicators": bullish,
        "bearish_indicators": bearish
    }