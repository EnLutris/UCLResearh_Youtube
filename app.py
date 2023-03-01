from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Literal
import os
from utils.youtube_comments import feriha

port = os.environ.get('PORT', 8000)
app = FastAPI(PORT = port)

class Item(BaseModel):
    url: str


@app.get("/")
async def status_check():
  return "alive"

@app.get("/comments")
async def data_format():
  return ("url should be submitted in quotes")

@app.post("/comments")
async def youtube_comments(url: str):
  print(url)
  comments = feriha(url)
  return comments