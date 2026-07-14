# ==========================================
# File : decision_engine.py
#
# Responsibility:
# Generate BUY / SELL / WAIT
# based on analyzed market.
# ==========================================

from src.models import Decision


def make_decision(market: dict) -> Decision:

    signal = "WAIT"
    reason = "Market is not ready."

    if market["trend"] == "BULLISH":
        signal = "BUY CE"
        reason = "Bullish trend confirmed."

    elif market["trend"] == "BEARISH":
        signal = "BUY PE"
        reason = "Bearish trend confirmed."

    return Decision(
        signal=signal,
        confidence=market["confidence"],
        reason=reason
    )