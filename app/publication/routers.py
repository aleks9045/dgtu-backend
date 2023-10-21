import aiofiles
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import FileResponse

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
            "details": "no articles"
        })


@router.post('/add_article')
async def add_article(
        new_article: article_schema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Article).values(**new_article.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post('/add_photo')
async def upload_photo(file: UploadFile = File(...)):
    file_path = f'static/{file.filename}'
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    return {"status": "success"}


@router.get('/get_photo')
async def photo(article_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Article.file_name).where(Article.id == article_id)
        result = await session.execute(query)
        file_name = result.scalars().all()[0]
        return FileResponse(path=f'static/{file_name}', filename=f'{file_name}', media_type='multipart/form-data')

    except Exception:
        raise HTTPException(status_code=501, detail={
            "status": "error",
            "data": None,
            "details": "no article with and photo with this id"
        })