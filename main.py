from typing import Annotated

from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from database import make_query
app = FastAPI()


@app.post("/api")
async def root(body: str = Body(..., media_type='text/plain')):
    # print(body)
    res = make_query(body)
    return {"result": res}
