"""
========================================================

File : candle_service.py

Purpose:
Fetch live market candles from Yahoo Finance.

Developer : Lohith Kumar

========================================================
"""

import yfinance as yf


def get_candles(symbol: str):

    # Mapping our symbols to Yahoo Finance symbols
    symbol_map = {
        "NIFTY": "^NSEI",
        "BANKNIFTY": "^NSEBANK",
        "RELIANCE": "RELIANCE.NS",
        "TCS": "TCS.NS",
        "INFY": "INFY.NS"
    }

    yahoo_symbol = symbol_map.get(symbol.upper(), "^NSEI")

    # Download latest candles
    df = yf.download(
        yahoo_symbol,
        period="5d",
        interval="5m",
        progress=False,
        auto_adjust=False
    )

    # Handle MultiIndex columns (yfinance >= 1.5.x)
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    # Remove rows with missing values
    df = df.dropna()

    candles = []

    for _, row in df.iterrows():

        candles.append({
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"])
        })

    return candles


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    candles = get_candles("NIFTY")

    print(f"Total Candles : {len(candles)}")

    if candles:
        print("\nLatest Candle:")
        print(candles[-1])
    else:
        print("No candle data received.")