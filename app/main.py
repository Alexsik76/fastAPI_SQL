from fastapi import FastAPI, Body, Response
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import make_query
from .queries import TABLES, COLUMNS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/sql")
async def root(body: str = Body(media_type='text/plain')):
    res = make_query(body)
    return {"result": res}


@app.get("/api/schema")
async def get_schema(response: Response):
    tables = make_query(TABLES)
    for table in tables:
        columns = make_query(COLUMNS % table['TABLE_NAME'])
        table['columns'] = columns
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cache-Control'] = 'no-cache'
    return {'tables': tables}
