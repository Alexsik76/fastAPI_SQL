from typing import Annotated

from fastapi import FastAPI, Body
from database import make_query
app = FastAPI()


@app.post("/api")
async def root(sql_query: Annotated[str, Body()]):
    res = make_query(sql_query)
    return {"res": res}
