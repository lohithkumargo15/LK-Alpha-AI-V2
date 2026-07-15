"""
=========================================================

File : settings.py

Purpose:
Central configuration for LK Alpha AI.

Reads secrets from .env file.

Developer : Lohith Kumar

=========================================================
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# ==========================================
# Project Information
# ==========================================

PROJECT_NAME = "LK Alpha AI"

PROJECT_DESCRIPTION = "AI Powered Intraday Trading Assistant"

VERSION = "2.0.0"

DEVELOPER = "Lohith Kumar"

TECHNICAL_LEAD = "ChatGPT"

# ==========================================
# Telegram Configuration
# ==========================================

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ==========================================
# TradingView Configuration
# ==========================================

TRADINGVIEW_WEBHOOK_SECRET = os.getenv("TRADINGVIEW_WEBHOOK_SECRET")

# ==========================================
# Application
# ==========================================

APP_MODE = "DEVELOPMENT"