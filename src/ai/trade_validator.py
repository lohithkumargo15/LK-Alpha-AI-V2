"""
========================================================

File : trade_validator.py

Purpose:
Final validation before trade signal.

Developer : Lohith Kumar

========================================================
"""


def validate_trade(market, decision):

    """
    Final AI validation.

    Returns:
    {
        valid,
        reason
    }
    """

    if decision.signal == "WAIT":

        return {
            "valid": False,
            "reason": "No trade signal."
        }

    if market.confidence < 60:

        return {
            "valid": False,
            "reason": "Confidence too low."
        }

    if market.trend == "SIDEWAYS":

        return {
            "valid": False,
            "reason": "Sideways market."
        }

    return {
        "valid": True,
        "reason": "Trade validated."
    }


if __name__ == "__main__":

    class Market:

        confidence = 85
        trend = "BULLISH"

    class Decision:

        signal = "BUY CE"

    print(validate_trade(
        Market(),
        Decision()
    ))