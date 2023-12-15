from pydantic import BaseModel, Json
from typing import Optional


class DataModel(BaseModel):
    date: str
    randomValue: int


class JsonModel(BaseModel):
    date: str = '{"date": "12.12.2023"}'


class AnyFormatModel(BaseModel):
    # js_data: Optional[str] = None
    # xml_data: Optional[str] = None
    format: str
    tree: str
