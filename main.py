import os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

#from routers import webhooks

app = FastAPI()

# app.include_router(webhooks.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
