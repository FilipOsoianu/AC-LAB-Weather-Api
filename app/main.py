from fastapi import FastAPI
from typing import List
from fastapi import FastAPI, Query
import requests
import json

from pydantic import BaseModel
from typing import List


class Forecast(BaseModel):
    weather:  List


async def request(client):
    response = await client.get(URL)
    return response.text


app = FastAPI()
URL = "https://fcc-weather-api.glitch.me/api/current?"





@app.get("/weather", response_model=Forecast)
async def get_model(lat: str = Query('15'), lon: str = Query('139')):
    requestURL = URL + 'lat=' + lat + '&lon=' + lon
    response = json.loads(requests.get(requestURL).text)
    print(response['weather'])
    return Forecast(weather=response['weather'])
