"""
========================================================

File : score_engine.py

Purpose:
Calculate Bullish and Bearish Scores.

Developer : Lohith Kumar

========================================================
"""

from src.ema import check_ema
from src.vwap import check_vwap
from src.option_chain import check_option_chain

from config.scores import SCORES


def calculate_score(data):

    bullish_score = 0
    bearish_score = 0

    # ==========================================
    # EMA
    # ==========================================

    ema = check_ema(data)

    if ema == "BULLISH":
        bullish_score += SCORES["EMA"]

    elif ema == "BEARISH":
        bearish_score += SCORES["EMA"]

    # ==========================================
    # VWAP
    # ==========================================

    vwap = check_vwap(
        data.ltp,
        data.vwap
    )

    if vwap == "BULLISH":
        bullish_score += SCORES["VWAP"]

    elif vwap == "BEARISH":
        bearish_score += SCORES["VWAP"]

    # ==========================================
    # BOS
    # ==========================================

    if data.bos == "BULLISH":
        bullish_score += SCORES["BOS"]

    elif data.bos == "BEARISH":
        bearish_score += SCORES["BOS"]

    # ==========================================
    # CHoCH
    # ==========================================

    if data.choch == "BULLISH":
        bullish_score += SCORES["CHOCH"]

    elif data.choch == "BEARISH":
        bearish_score += SCORES["CHOCH"]

    # ==========================================
    # FVG
    # ==========================================

    if data.fvg == "BULLISH":
        bullish_score += SCORES["FVG"]

    elif data.fvg == "BEARISH":
        bearish_score += SCORES["FVG"]

    # ==========================================
    # Order Block
    # ==========================================

    if data.order_block == "BULLISH":
        bullish_score += SCORES["ORDER_BLOCK"]

    elif data.order_block == "BEARISH":
        bearish_score += SCORES["ORDER_BLOCK"]

    # ==========================================
    # Liquidity Sweep
    # ==========================================

    if data.liquidity == "BULLISH":
        bullish_score += SCORES["LIQUIDITY"]

    elif data.liquidity == "BEARISH":
        bearish_score += SCORES["LIQUIDITY"]

    # ==========================================
    # Option Chain
    # ==========================================

    option = check_option_chain(data)

    if option["bullish"]:
        bullish_score += SCORES["OPTION_CHAIN"]

    if option["bearish"]:
        bearish_score += SCORES["OPTION_CHAIN"]

    # ==========================================
    # Volume
    # ==========================================

    if data.volume_signal == "BULLISH":
        bullish_score += SCORES["VOLUME"]

    elif data.volume_signal == "BEARISH":
        bearish_score += SCORES["VOLUME"]

    # ==========================================
    # Final Score
    # ==========================================

    return {
        "bullish": bullish_score,
        "bearish": bearish_score
    }