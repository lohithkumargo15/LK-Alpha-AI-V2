# ==========================================
# File : choch.py
#
# Responsibility:
# Detect Change of Character
# ==========================================

def check_choch(data):

    # Temporary logic.
    # Later this will use swing highs/lows.

    if data.ema_9 > data.ema_20:
        return "BULLISH"

    elif data.ema_9 < data.ema_20:
        return "BEARISH"

    return "NONE"