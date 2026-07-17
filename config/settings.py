"""
========================================================

LK Alpha AI Configuration

Developer : Lohith Kumar

========================================================
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

PROJECT_NAME = "LK Alpha AI"

PROJECT_DESCRIPTION = "AI Powered Intraday Trading Assistant"

VERSION = "2.0.0"

DEVELOPER = "Lohith Kumar"

TECHNICAL_LEAD = "ChatGPT"

# ==========================================
# Telegram Configuration
# ==========================================

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")