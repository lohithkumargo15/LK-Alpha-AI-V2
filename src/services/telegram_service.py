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

    # -------------------------------
    # Check Configuration
    # -------------------------------

    if settings.TELEGRAM_BOT_TOKEN == "":
        print("❌ Telegram Bot Token not configured.")
        return None

    if settings.TELEGRAM_CHAT_ID == "":
        print("❌ Telegram Chat ID not configured.")
        return None

    # -------------------------------
    # Telegram API URL
    # -------------------------------

    url = (
        f"https://api.telegram.org/bot"
        f"{settings.TELEGRAM_BOT_TOKEN}"
        f"/sendMessage"
    )

    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    # -------------------------------
    # Send Message
    # -------------------------------

    try:

        response = requests.post(
            url=url,
            json=payload,
            timeout=15
        )

        print("\n==============================")
        print("Telegram Debug")
        print("==============================")
        print("URL :", url)
        print("Chat ID :", settings.TELEGRAM_CHAT_ID)
        print("Status Code :", response.status_code)
        print("Response :", response.text)
        print("==============================\n")

        response.raise_for_status()

        print("✅ Telegram message sent successfully.")

        return response.json()

    except Exception as e:

        print("❌ Telegram Exception")
        print(e)

        return None