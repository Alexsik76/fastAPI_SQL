from fastapi import FastAPI, Body
import queries
from database import make_query
app = FastAPI()


@app.post("/api")
async def root(body: str = Body(media_type='text/plain')):
    res = make_query(body)
    return {"result": res}


@app.get("/api/schema")
async def get_schema():
    tables = make_query(queries.TABLES)
    table = "car"
    q = queries.COLUMNS % table
    columns = make_query(q)
    return {"tables": tables,
            "columns": columns}
