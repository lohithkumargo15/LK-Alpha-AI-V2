"""
========================================================

File : analyze.py

Purpose:
Analyze Market using LK Alpha AI

Developer : Lohith Kumar

========================================================
"""

from fastapi import APIRouter


from src.ai.market_analyzer import analyze_market
from src.ai.decision_engine import make_decision
from src.risk.risk_manager import calculate_risk
from src.ai.health_engine import get_health
from src.services.tradingview_service import get_market_data

router = APIRouter()


@router.get("/analyze/{symbol}")
def analyze(symbol: str):

    # -----------------------------------------
    # Get Live Market Data
    # -----------------------------------------

    market_input = get_market_data(symbol)

    # -----------------------------------------
    # Analyze Market
    # -----------------------------------------

    market = analyze_market(market_input)

    # -----------------------------------------
    # Generate Decision
    # -----------------------------------------

    decision = make_decision(market)

    # -----------------------------------------
    # Calculate Risk
    # -----------------------------------------

    risk = calculate_risk(
        decision.signal,
        market_input
    )

    # -----------------------------------------
    # AI Health
    # -----------------------------------------

    health = get_health(market_input)

    # -----------------------------------------
    # Final Response
    # -----------------------------------------

    return {

        "project": "LK Alpha AI",

        "symbol": symbol,

        "market_input": {
            "ltp": market_input.ltp,
            "ema_9": market_input.ema_9,
            "ema_20": market_input.ema_20,
            "vwap": market_input.vwap,
            "atr": market_input.atr,
            "bos": market_input.bos,
            "choch": market_input.choch,
            "fvg": market_input.fvg,
            "order_block": market_input.order_block,
            "liquidity": market_input.liquidity,
            "volume_signal": market_input.volume_signal,

            # NEW
            "support": market_input.support,
            "resistance": market_input.resistance
        },

        "market": market.model_dump(),

        "decision": decision.model_dump(),

        "risk": risk,

        "health": health
    }