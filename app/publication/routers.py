from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
import aiofiles

from app.database import get_async_session
from app.publication.models import Article
from app.publication.schemas import article_schema

router = APIRouter(
    prefix="/articles",
    tags=["Articles"]
)


@router.get('/all')
async def get_all_articles(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Article)
        result = await session.execute(query)

        return {
            "status": "success",
            "data": result.scalars().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

