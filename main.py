from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

import queries
from database import make_query
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/sql")
async def root(body: str = Body(media_type='text/plain')):
    res = make_query(body)
    return {"result": res}


@app.get("/api/schema")
async def get_schema():
    tables = make_query(queries.TABLES)
    for table in tables:
        columns = make_query(queries.COLUMNS % table['TABLE_NAME'])
        table['columns'] = columns
    return tables
