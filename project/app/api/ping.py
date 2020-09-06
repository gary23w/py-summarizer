# project/app/api/ping.py


from fastapi import APIRouter, Depends, HTTPException, Path, BackgroundTasks

from app.config import get_settings, Settings
from app.api import crud
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema
from app.summarizer import generate_summary


router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@router.get("/fuck")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "fuck": "you",
        "environment": "settings.environment",
        "testing": "settings.testing",
    }

