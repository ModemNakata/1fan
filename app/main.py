from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import os

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/mydatabase"
)

# Create async engine
engine = create_async_engine(DATABASE_URL)

app = FastAPI()


@app.get("/")
async def get_database_status():
    """Simple endpoint to check database connection status"""
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        return {"database_status": "connected"}
    except Exception as e:
        return {"database_status": "disconnected", "error": str(e)}
