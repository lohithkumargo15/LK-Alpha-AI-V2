# ==========================================
# LK Alpha AI
# Main Application
#
# Entry Point of the Project
# ==========================================

from fastapi import FastAPI

from config import settings

from src.market_analyzer import analyze_market
from src.decision_engine import make_decision
from src.webhook import router as webhook_router
from src.risk_manager import calculate_risk
from src.models import MarketInput
from src.tradingview_service import get_market_data
from src.telegram_service import send_telegram_message
from src.message_builder import build_trade_message


# ------------------------------------------
# Create FastAPI Application
# ------------------------------------------

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION
)

# Register all routers

app.include_router(webhook_router)


# ------------------------------------------
# Home API
# ------------------------------------------

@app.get("/", tags=["Home"])
def home_page():

    market_input = get_market_data("NIFTY")

    market = analyze_market(market_input)

    decision = make_decision(market.model_dump())

    risk = calculate_risk(
        decision.signal,
        market_input
    )

    message = build_trade_message(
    market,
    decision,
    risk
    )

    send_telegram_message(message)

    return {
        "project": settings.PROJECT_NAME,
        "developer": settings.DEVELOPER,
        "market": market.model_dump(),
        "decision": decision.model_dump(),
        "risk": risk
    }