from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    titulo: str
    director: str
    productora: str
    añoLanzamiento: str