from pydantic import BaseModel


class DataModel(BaseModel):
    date: str
    randomValue: int


class AnyFormatModel(BaseModel):
    format: str = 'json | xml'
    data: str
