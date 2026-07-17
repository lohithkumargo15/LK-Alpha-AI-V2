"""
========================================================

File : multi_timeframe.py

Purpose:
Multi Timeframe Confirmation

Developer : Lohith Kumar

========================================================
"""


def analyze_timeframes(tf1, tf5, tf15):

    """
    Returns overall market trend
    based on multiple timeframes.
    """

    trends = [tf1, tf5, tf15]

    bullish = trends.count("BULLISH")
    bearish = trends.count("BEARISH")

    if bullish >= 2:
        return {
            "trend": "BULLISH",
            "confidence": 90
        }

    if bearish >= 2:
        return {
            "trend": "BEARISH",
            "confidence": 90
        }

    return {
        "trend": "SIDEWAYS",
        "confidence": 50
    }


if __name__ == "__main__":

    result = analyze_timeframes(
        "BULLISH",
        "BULLISH",
        "BEARISH"
    )

    print(result)