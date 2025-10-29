from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import os

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL"  # , "postgresql+asyncpg://user:password@db:5432/mydatabase"
)

# Create async engine
engine = create_async_engine(DATABASE_URL)

app = FastAPI()

# Mount static files
# (if you want FastAPI to serve them too, but nginx is better)
#
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")


# Favicon redirect
@app.get("/favicon.ico")
async def favicon_redirect():
    return RedirectResponse(
        url="/static/favicon-moon100x3_886799.svg",
        status_code=status.HTTP_301_MOVED_PERMANENTLY,
    )  # default 307 moved temporary


@app.get("/", response_class=HTMLResponse)
async def get_database_status(request: Request):
    """Render template with database connection status"""
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        db_status = "connected"
        error = None
    except Exception as e:
        db_status = "disconnected"
        error = str(e)

    return templates.TemplateResponse(
        "index.html", {"request": request,
                       "db_status": db_status, "error": error}
    )


@app.get("/api/status")
async def api_status():
    """JSON endpoint for API clients"""
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        return {"database_status": "connected"}
    except Exception as e:
        return {"database_status": "disconnected", "error": str(e)}
