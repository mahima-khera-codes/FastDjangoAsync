from fastapi import FastAPI
from datetime import datetime
from schemas import Schema
import pytz
import httpx

app = FastAPI()


@app.get("/get-response")
async def get_response_from_backend(input_start: datetime):
    timezone = pytz.timezone("Europe/Moscow")
    if isinstance(input_start, datetime):
        input_start = input_start.astimezone(timezone)

    target_url = "http://localhost:8000/filtered-endpoint-states/"
    async with httpx.AsyncClient() as client:
        response = await client.get(
            target_url, params={"input_start": input_start.isoformat()}
        )
    return response.json()
