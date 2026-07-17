"""
========================================================

Risk Manager

Uses ATR to calculate
dynamic SL and Targets.

========================================================
"""


def calculate_risk(signal, market):

    entry = market.ltp

    atr = market.atr

    if signal == "BUY CE":

        stop = round(entry - atr, 2)

        target1 = round(entry + atr * 2, 2)

        target2 = round(entry + atr * 3, 2)

    elif signal == "BUY PE":

        stop = round(entry + atr, 2)

        target1 = round(entry - atr * 2, 2)

        target2 = round(entry - atr * 3, 2)

    else:

        stop = 0
        target1 = 0
        target2 = 0

    return {
        "entry": entry,
        "stop_loss": stop,
        "target_1": target1,
        "target_2": target2,
        "risk_reward": "1:2"
    }