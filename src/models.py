from pydantic import BaseModel
from typing import List


class AnyFormatModel(BaseModel):
    tree: List[str]
