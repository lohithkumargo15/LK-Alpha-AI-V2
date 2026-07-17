"""
========================================================

File : logger.py

Purpose:
Central Logging Utility

Developer : Lohith Kumar

========================================================
"""

from datetime import datetime


def log(level: str, message: str):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{now}] [{level}] {message}")


def info(message: str):
    log("INFO", message)


def warning(message: str):
    log("WARNING", message)


def error(message: str):
    log("ERROR", message)


if __name__ == "__main__":

    info("LK Alpha AI Started")

    warning("Market is Sideways")

    error("Yahoo Finance Connection Failed")