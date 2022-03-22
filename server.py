from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from summary_gen import generate_summary

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

@app.get("/summary/")
def summary(q: str):
    return generate_summary(q)


