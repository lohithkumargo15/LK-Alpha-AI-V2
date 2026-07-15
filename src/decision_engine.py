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
    reason = "Market is not ready."

    if market.trend == "BULLISH":
        signal = "BUY CE"
        reason = "Bullish trend confirmed."

    elif market.trend == "BEARISH":
        signal = "BUY PE"
        reason = "Bearish trend confirmed."

    return Decision(
        signal=signal,
        confidence=market.confidence,
        reason=reason
    )