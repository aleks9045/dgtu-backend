from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.articles.models import file

router = APIRouter(
    prefix="/articles",
    tags=["Articles"]
)


@router.get('/all')
async def get_all_files(session: AsyncSession = Depends(get_async_session)):
    query = select(file)
    result = await session.execute(query)
    return result.all()
