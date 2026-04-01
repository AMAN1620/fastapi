from .config import Settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

settings = Settings()
engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def connect_to_db():
    async with SessionLocal() as session:
        yield session





# Short notes:
# - `create_engine()` is for synchronous database connections.
# - This file currently uses the sync PostgreSQL driver: `postgresql+psycopg://...`.
# - If you switch to `postgresql+asyncpg://...`, then use:
#   `create_async_engine()` and `AsyncSession` from `sqlalchemy.ext.asyncio`.
# - Sync setup: `create_engine()` + normal `Session`
# - Async setup: `create_async_engine()` + `AsyncSession` + `await db.execute(...)`