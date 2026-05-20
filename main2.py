from os import name

from sqlalchemy import select
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import query
from database import engine, get_db
from models import UserModel, Base
from schemas import UserCreateSchema, UserResponseSchema
from contextlib import asynccontextmanager

@asynccontextmanager
async def create_db(app: FastAPI):
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=create_db)

@app.get("/{name}", response_model=UserResponseSchema)
async def firstUser(name: str, db: AsyncSession = Depends(get_db)):
    queryk = select(UserModel).where(UserModel.username == f"{name}")
    result = await db.execute(queryk)
    user = result.scalars().one_or_none()
    return user