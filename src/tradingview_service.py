"""
========================================================

File : tradingview_service.py

Purpose:
Acts as the bridge between TradingView
and LK Alpha AI.

Currently returns sample market data.

Later this file will fetch live market
data from TradingView/API.

========================================================
"""

from src.models import MarketInput
from src.candle_service import get_candles
from src.ema import calculate_ema
from src.vwap import calculate_vwap
from src.atr import calculate_atr
from src.bos import check_bos

def get_market_data(symbol: str) -> MarketInput:

    candles = get_candles(symbol)

    latest = candles[-1]

    ema9 = calculate_ema(candles, 9)
    ema20 = calculate_ema(candles, 20)
    vwap = calculate_vwap(candles)
    atr = calculate_atr(candles)
    bos = check_bos(candles)

    return MarketInput(
        symbol=symbol,
        ltp=latest["close"],
        ema_9=ema9,
        ema_20=ema20,
        vwap=vwap,
        volume=latest["volume"],
        atr=atr,
        bos=bos
    )