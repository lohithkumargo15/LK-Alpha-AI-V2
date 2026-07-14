"""
========================================================

File : message_builder.py

Purpose:
Build a readable Telegram message.

Developer : Lohith Kumar

========================================================
"""


def build_trade_message(market, decision, risk):

    message = f"""
🚀 LK Alpha AI

📊 Symbol : {market.symbol}

📈 Trend : {market.trend}

🎯 Signal : {decision.signal}

✅ Confidence : {decision.confidence}%

💰 Entry : {risk['entry']}

🛑 Stop Loss : {risk['stop_loss']}

🥇 Target 1 : {risk['target_1']}

🥈 Target 2 : {risk['target_2']}

⚖ Risk Reward : {risk['risk_reward']}
"""

    return message