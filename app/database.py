from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config

DATABASE_URL = config("PG_URL")

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
