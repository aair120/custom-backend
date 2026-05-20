from sqlalchemy import create_engine, URL , text
from config import settings
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    pool_size=5
    )

sessionlocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with sessionlocal() as session:
        yield session
