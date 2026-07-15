"""
========================================================

File : indicator_engine.py

Purpose:
Calculate all market indicators.

Developer : Lohith Kumar

========================================================
"""

from src.ema import calculate_ema
from src.vwap import calculate_vwap
from src.atr import calculate_atr
from src.bos import check_bos
from src.choch import check_choch
from src.fvg import check_fvg
from src.order_block import check_order_block
from src.liquidity import check_liquidity
from src.volume import check_volume


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