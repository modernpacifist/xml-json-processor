from pydantic import BaseModel


class AnyFormatModel(BaseModel):
    tree: str
