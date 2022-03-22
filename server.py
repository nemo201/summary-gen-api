from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from summary_gen import generate_summary
from pydantic import BaseModel

app = FastAPI()

origins = [
"*",
"http://localhost.tiangolo.com",
"https://localhost.tiangolo.com",
"http://localhost",
"http://localhost:8080",
]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

class Item(BaseModel):
    text: str
      


@app.post("/summary/")
def summary(item: Item):
    return generate_summary(item.text)


@app.post("/items/")
async def create_item(item: Item):
    return item


