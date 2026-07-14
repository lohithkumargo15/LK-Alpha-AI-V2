"""
========================================================

File : telegram_service.py

Purpose:
Send trading alerts to Telegram.

Developer : Lohith Kumar

========================================================
"""

import requests

from config import settings


def send_telegram_message(message: str):
    
    # If Telegram is not configured,
    # simply skip sending the message.

    if settings.TELEGRAM_BOT_TOKEN == "":
        print("Telegram Bot Token not configured.")
        return

    if settings.TELEGRAM_CHAT_ID == "":
        print("Telegram Chat ID not configured.")
        return

    url = (
        f"https://api.telegram.org/bot"
        f"{settings.TELEGRAM_BOT_TOKEN}"
        f"/sendMessage"
    )

    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)

    return response.json()