"""
========================================================

File : support_resistance.py

Purpose:
Detect Support & Resistance Levels

Developer : Lohith Kumar

========================================================
"""


def find_support_resistance(candles):

    """
    Finds simple support and resistance.

    Returns:
    {
        support,
        resistance
    }
    """

    lows = [c["low"] for c in candles]
    highs = [c["high"] for c in candles]

    support = min(lows)
    resistance = max(highs)

    return {
        "support": round(support, 2),
        "resistance": round(resistance, 2)
    }


if __name__ == "__main__":

    sample = [

        {"low": 100, "high": 110},
        {"low": 98, "high": 112},
        {"low": 99, "high": 108},
        {"low": 101, "high": 115},
        {"low": 97, "high": 111}

    ]

    result = find_support_resistance(sample)

    print(result)