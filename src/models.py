from pydantic import BaseModel, Json
from typing import Optional


class DataModel(BaseModel):
    date: str
    randomValue: int


class JsonModel(BaseModel):
    date: str = '{"date": "12.12.2023"}'


class AnyFormatModel(BaseModel):
    format: str
    tree: str
