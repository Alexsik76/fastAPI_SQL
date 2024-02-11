from pydantic import BaseModel


class Column(BaseModel):
    COLUMN_NAME: str
    DATA_TYPE: str


class Table(BaseModel):
    TABLE_NAME: str
    COLUMNS: list[Column]
