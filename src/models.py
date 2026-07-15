from pydantic import BaseModel


class MarketData(BaseModel):
    symbol: str
    trend: str
    market_status: str
    confidence: int
    strength: str


class Decision(BaseModel):
    signal: str
    confidence: int
    reason: str

class Risk(BaseModel):
    entry: float
    stop_loss: float
    target_1: float
    target_2: float
    risk_reward: str

class MarketInput(BaseModel):
    symbol: str
    ltp: float
    ema_9: float
    ema_20: float
    vwap: float
    volume: int
    volume_signal: str
    atr: float   
    bos: str
    choch: str
    fvg: str
    order_block: str
    liquidity: str