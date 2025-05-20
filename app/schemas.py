from pydantic import BaseModel

class Produto(BaseModel):
    item: str
    preço: float