from src.ema import check_ema
from src.vwap import check_vwap
from src.volume import check_volume
from src.bos import check_bos
from src.choch import check_choch
from src.fvg import check_fvg
from src.order_block import check_order_block
from src.option_chain import check_option_chain


def calculate_score(data):

    bullish_score = 0
    bearish_score = 0

    # EMA

    ema = check_ema(data)

    if ema == "BULLISH":
        bullish_score += 25

    elif ema == "BEARISH":
        bearish_score += 25

    # VWAP

    vwap = check_vwap(data)

    if vwap == "BULLISH":
        bullish_score += 20

    elif vwap == "BEARISH":
        bearish_score += 20


    # BOS

    bos = data.bos

    if bos == "BULLISH":
        bullish_score += 20

    elif bos == "BEARISH":
        bearish_score += 20    

    # CHoCH

    choch = check_choch(data)

    if choch == "BULLISH":
        bullish_score += 15

    elif choch == "BEARISH":
        bearish_score += 15    


    # FVG

    if check_fvg(data):
        bullish_score += 10

    # Order Block

    if check_order_block(data):
        bullish_score += 10

    # Option Chain

    option = check_option_chain(data)

    if option["bullish"]:
        bullish_score += 20

    if option["bearish"]:
        bearish_score += 20

    # Volume

    if check_volume(data):
        bullish_score += 15
        bearish_score += 15

    return {
        "bullish": bullish_score,
        "bearish": bearish_score
    }