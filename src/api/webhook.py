"""
========================================================

File : webhook.py

Purpose:
TradingView Webhook

Developer : Lohith Kumar

========================================================
"""

from fastapi import APIRouter

from src.models import MarketInput
from src.ai.market_analyzer import analyze_market
from src.ai.decision_engine import make_decision
from src.risk.risk_manager import calculate_risk
from src.ai.trade_validator import validate_trade
from src.ai.health_engine import get_health
from src.services.telegram_service import send_telegram_message

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"]
)


@router.post("/tradingview")
def tradingview_webhook(data: MarketInput):

    # -------------------------------
    # Analyze Market
    # -------------------------------

    market = analyze_market(data)

    # -------------------------------
    # AI Decision
    # -------------------------------

    decision = make_decision(market)

    # -------------------------------
    # Validate Trade
    # -------------------------------

    validation = validate_trade(
        market,
        decision
    )

    # -------------------------------
    # Risk Management
    # -------------------------------

    risk = calculate_risk(
        decision.signal,
        data
    )

    # -------------------------------
    # Market Health
    # -------------------------------

    health = get_health(data)

    # -------------------------------
    # Telegram Notification
    # -------------------------------

    if validation["valid"]:

        message = f"""
🚀 LK Alpha AI

📈 Symbol : {data.symbol}

📢 Signal : {decision.signal}

🎯 Confidence : {decision.confidence}%

💰 Entry : {risk['entry']}
🛑 Stop Loss : {risk['stop_loss']}
🎯 Target 1 : {risk['target_1']}
🎯 Target 2 : {risk['target_2']}

📊 Trend : {market.trend}
💪 Strength : {market.strength}

📝 Reason:
{decision.reason}
"""

        send_telegram_message(message)

    return {

        "market": market.model_dump(),

        "decision": decision.model_dump(),

        "validation": validation,

        "risk": risk,

        "health": health

    }