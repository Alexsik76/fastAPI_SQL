from typing import Callable

from fastapi import Body, FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import make_query, make_insert
from .models import Table
from .queries import TABLES, COLUMNS


class ValidationErrorLoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except RequestValidationError as exc:
                body = await request.body()
                detail = {"errors": exc.errors(), "body": body.decode()}
                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler


app = FastAPI()
router = APIRouter(route_class=ValidationErrorLoggingRoute)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,# noqa Expected type
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/sql")
async def root(body: str = Body(media_type='text/plain')):
    if body.lower().startswith('select'):
        res = make_query(body)
    else:
        res = make_insert(body)
    return res


@app.get("/api/schema", response_model=list[Table])
async def get_schema():
    tables = make_query(TABLES)
    for table in tables:
        columns = make_query(COLUMNS % table['TABLE_NAME'])
        table['COLUMNS'] = columns
    return tables
