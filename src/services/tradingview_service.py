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
from src.services.candle_service import get_candles
from src.indicators.indicator_engine import calculate_indicators
from src.indicators.support_resistance import find_support_resistance



def get_market_data(symbol: str) -> MarketInput:

    # -----------------------------------------
    # Fetch Candle Data
    # -----------------------------------------

    candles = get_candles(symbol)

    latest = candles[-1]

    # -----------------------------------------
    # Calculate Indicators
    # -----------------------------------------

    indicators = calculate_indicators(candles)

    # -----------------------------------------
    # Support & Resistance
    # -----------------------------------------

    sr = find_support_resistance(candles)

    # -----------------------------------------
    # Return Market Input
    # -----------------------------------------

    return MarketInput(

        symbol=symbol,

        ltp=latest["close"],

        volume=latest["volume"],

        support=sr["support"],

        resistance=sr["resistance"],

        **indicators

    )