from pydantic import BaseModel


class DataModel(BaseModel):
    date: str
    randomValue: int
