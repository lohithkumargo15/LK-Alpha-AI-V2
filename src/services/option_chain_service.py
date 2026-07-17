"""
========================================================

File : option_chain_service.py

Purpose:
Fetch Option Chain Data.

Current Version:
Returns dummy data.

Future Version:
Fetch live Option Chain from
Upstox / Angel One API.

Developer : Lohith Kumar

========================================================
"""


def get_option_chain(symbol: str):

    """
    Returns Option Chain Data.

    Future:
    Replace this with broker API.
    """

    return {

        "symbol": symbol,

        "pcr": 1.02,

        "max_pain": 24100,

        "call_oi": 245000,

        "put_oi": 268000,

        "call_change_oi": 15000,

        "put_change_oi": 22000,

        "call_writing": False,

        "put_writing": True,

        "bullish": True,

        "bearish": False
    }


if __name__ == "__main__":

    data = get_option_chain("NIFTY")

    print("\nOption Chain\n")

    for key, value in data.items():
        print(f"{key:18}: {value}")