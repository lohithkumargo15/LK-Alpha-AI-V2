"""
========================================================

File : paper_trading.py

Purpose:
Paper Trading Engine

Developer : Lohith Kumar

========================================================
"""


class PaperTrader:

    def __init__(self):

        self.balance = 100000

        self.trades = []

    def buy(self, symbol, price):

        self.trades.append({

            "type": "BUY",

            "symbol": symbol,

            "price": price

        })

        print(f"BUY {symbol} @ {price}")

    def sell(self, symbol, price):

        self.trades.append({

            "type": "SELL",

            "symbol": symbol,

            "price": price

        })

        print(f"SELL {symbol} @ {price}")

    def summary(self):

        print("\n========== PAPER TRADING ==========")

        print(f"Balance : {self.balance}")

        print(f"Trades  : {len(self.trades)}")

        for trade in self.trades:

            print(trade)


if __name__ == "__main__":

    trader = PaperTrader()

    trader.buy("NIFTY", 25000)

    trader.sell("NIFTY", 25120)

    trader.summary()