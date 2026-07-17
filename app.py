from fastapi import FastAPI

from config.settings import (
    PROJECT_NAME,
    PROJECT_DESCRIPTION,
    VERSION
)

from src.api.webhook import router as webhook_router
from src.api.analyze import router as analyze_router

app = FastAPI(
    title=PROJECT_NAME,
    description=PROJECT_DESCRIPTION,
    version=VERSION
)

app.include_router(webhook_router)
app.include_router(analyze_router)


@app.get("/")
def root():
    return {
        "project": PROJECT_NAME,
        "version": VERSION,
        "status": "Running"
    }