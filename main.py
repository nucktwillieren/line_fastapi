import os
import uvicorn

from fastapi import FastAPI

#from route.linebot import router
from infra.mqtt.listener import Listener
from secrets import scope, username, password

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()


app = FastAPI()

# app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    mqtt_listener = Listener(scope, username, password)
    mqtt_listener.run()
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
