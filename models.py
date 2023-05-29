from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int
    titulo: str = Field(default = "Título", min_lenght = 2, max_length = 20)
    director: str = Field(default = "Director", min_lenght = 10, max_length = 25)
    productora: str = Field(default = "Productora", min_lenght = 10, max_length = 25)
    categoria: str = Field(default = "Categoria", min_lenght = 10, max_length = 35)
    anoLanzamiento: int = Field(default = "Año", le = 2023, ge = 1890)

    class Config:
        schema_extra = {
            "example": {
                "id": 12981,
                "titulo": "El Titanic",
                "director": "James Cameron",
                "productora": "James Cameron",
                "categoria": "Romance, Drama",
                "anoLanzamiento": 1997
            }
        }