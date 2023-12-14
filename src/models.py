from pydantic import BaseModel


class JsonModel(BaseModel):
    date: str
    randomValue: int
