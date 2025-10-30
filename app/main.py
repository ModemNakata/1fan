from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from sqlalchemy import text
from database import engine

# from routers import ...
import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

# Include routers
# app.include_router(....router, prefix="/...", tags=["..."])

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
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/me", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("me.html", {"request": request})
