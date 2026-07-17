"""
========================================================

File : decision_engine.py

Purpose:
Generate BUY / SELL / WAIT decision
based on analyzed market.

Developer : Lohith Kumar

========================================================
"""

from src.models import Decision, MarketData


def make_decision(market: MarketData) -> Decision:

    signal = "WAIT"
    confidence = market.confidence
    reason = "Market is not ready."

    # -----------------------------------------
    # Strong Bullish
    # -----------------------------------------

    if market.trend == "BULLISH":

        if confidence >= 80:
            signal = "BUY CE"
            reason = "Strong bullish confirmation."

        elif confidence >= 60:
            signal = "BUY CE"
            reason = "Bullish trend detected."

        else:
            signal = "WAIT"
            reason = "Bullish trend but confidence is low."

    # -----------------------------------------
    # Strong Bearish
    # -----------------------------------------

    elif market.trend == "BEARISH":

        if confidence >= 80:
            signal = "BUY PE"
            reason = "Strong bearish confirmation."

        elif confidence >= 60:
            signal = "BUY PE"
            reason = "Bearish trend detected."

        else:
            signal = "WAIT"
            reason = "Bearish trend but confidence is low."

    # -----------------------------------------
    # Sideways
    # -----------------------------------------

    else:

        signal = "WAIT"
        reason = "Sideways market."

    return Decision(
        signal=signal,
        confidence=confidence,
        reason=reason
    )