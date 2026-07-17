"""
========================================================

File : option_chain.py

Purpose:
Analyze Option Chain Data.

Developer : Lohith Kumar

========================================================
"""

from src.services.option_chain_service import get_option_chain


def check_option_chain(data):

    """
    Analyze Option Chain.

    Returns:
    {
        bullish: bool,
        bearish: bool
    }
    """

    option = get_option_chain(data.symbol)

    bullish = False
    bearish = False

    # ------------------------------------
    # PCR Analysis
    # ------------------------------------

    if option["pcr"] > 1:
        bullish = True

    elif option["pcr"] < 0.8:
        bearish = True

    # ------------------------------------
    # OI Writing
    # ------------------------------------

    if option["put_writing"]:
        bullish = True

    if option["call_writing"]:
        bearish = True

    return {
        "bullish": bullish,
        "bearish": bearish
    }


if __name__ == "__main__":

    class Dummy:

        symbol = "NIFTY"

    result = check_option_chain(Dummy())

    print(result)