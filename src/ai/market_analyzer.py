from src.models import MarketData, MarketInput
from src.ai.score_engine import calculate_score
from src.ai.market_strength import calculate_market_strength


def analyze_market(data: MarketInput) -> MarketData:

    score = calculate_score(data)
    strength = calculate_market_strength(score)

    trend = "SIDEWAYS"
    confidence = max(score["bullish"], score["bearish"])
    status = "WAIT"

    if score["bullish"] >= 60:
        trend = "BULLISH"
        status = "READY"

    elif score["bearish"] >= 60:
        trend = "BEARISH"
        status = "READY"

    return MarketData(
        symbol=data.symbol,
        trend=trend,
        market_status=status,
        confidence=confidence,
        strength=strength
    )