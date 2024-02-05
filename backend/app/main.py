from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from .database import make_query

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"please, go to ": "localhost:8000/docs"}


@app.post("/api/sql")
async def root(body: str = Body(media_type='text/plain')):
    response = make_query(body)
    return {"data": response}
