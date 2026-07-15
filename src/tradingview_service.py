"""
========================================================

File : tradingview_service.py

Purpose:
Acts as the bridge between TradingView
and LK Alpha AI.

Developer : Lohith Kumar

========================================================
"""

from src.models import MarketInput
from src.candle_service import get_candles
from src.indicator_engine import calculate_indicators


def get_market_data(symbol: str) -> MarketInput:

    # Fetch Candle Data
    candles = get_candles(symbol)

    latest = candles[-1]

    # Calculate All Indicators
    indicators = calculate_indicators(candles)

    return MarketInput(
        symbol=symbol,
        ltp=latest["close"],
        volume=latest["volume"],
        **indicators
    )