from fastapi import APIRouter
from src.models import MarketInput
from src.market_analyzer import analyze_market
from src.decision_engine import make_decision
from src.risk_manager import calculate_risk

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"]
)


@router.post("/tradingview")
def tradingview_webhook(data: MarketInput):

    market = analyze_market(data)

    decision = make_decision(market.model_dump())

    risk = calculate_risk(decision.signal)

    return {
        "market": market.model_dump(),
        "decision": decision.model_dump(),
        "risk": risk
    }