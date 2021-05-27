import os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn
import sql_app.database as db
import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers import webhooks, users

logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup() -> None:
    await db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.database.disconnect()

app.include_router(webhooks.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/liff", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0"
                , port=5000, reload=True
                )
