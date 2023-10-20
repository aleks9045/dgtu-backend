from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session

router = APIRouter(
    prefix="/articles",
    tags=["Articles"]
)

