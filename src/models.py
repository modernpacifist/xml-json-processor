from pydantic import BaseModel, Json


class DataModel(BaseModel):
    date: str
    randomValue: int


class JsonModel(BaseModel):
    date: str = '{"date": "12.12.2023"}'


class AnyFormatModel(BaseModel):
    format: str = "json | xml"
    data: str = '{"date": "12.12.2023"}'
