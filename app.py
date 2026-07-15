# ==========================================
# LK Alpha AI
# Main Application
#
# Entry Point of the Project
# ==========================================

from fastapi import FastAPI

from config import settings

from src.webhook import router as webhook_router
from src.analyze import router as analyze_router


# ------------------------------------------
# Create FastAPI Application
# ------------------------------------------

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION
)


# ------------------------------------------
# Register Routers
# ------------------------------------------

app.include_router(webhook_router)
app.include_router(analyze_router)


# ------------------------------------------
# Home API
# ------------------------------------------

@app.get("/", tags=["Home"])
def home_page():

    return {
        "project": settings.PROJECT_NAME,
        "description": settings.PROJECT_DESCRIPTION,
        "version": settings.VERSION,
        "developer": settings.DEVELOPER,
        "status": "Running Successfully",
        "message": "Welcome to LK Alpha AI 🚀"
    }