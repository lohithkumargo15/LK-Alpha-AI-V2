"""
========================================================

File : indicator_engine.py

Purpose:
Calculate all market indicators.

Developer : Lohith Kumar

========================================================
"""

from src.indicators.ema import calculate_ema
from src.indicators.vwap import calculate_vwap
from src.indicators.atr import calculate_atr
from src.indicators.bos import check_bos
from src.indicators.choch import check_choch
from src.indicators.fvg import check_fvg
from src.indicators.order_block import check_order_block
from src.indicators.liquidity import check_liquidity
from src.indicators.volume import check_volume


def calculate_indicators(candles):

    indicators = {

        "ema_9": calculate_ema(candles, 9),

        "ema_20": calculate_ema(candles, 20),

        "vwap": calculate_vwap(candles),

        "atr": calculate_atr(candles),

        "bos": check_bos(candles),

        "choch": check_choch(candles),

        "fvg": check_fvg(candles),

        "order_block": check_order_block(candles),

        "liquidity": check_liquidity(candles),

        "volume_signal": check_volume(candles)

    }

    return indicators