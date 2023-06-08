from typing import Optional
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from starlette.requests import Request

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

class User(BaseModel):
    email: str = Field(description="Email address", regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password: str = Field(description="Password", min_length=8)

    class Config:
        schema_extra = {
            "example": {
                "email": "juan@gmail.com",
                "password": "my_secret_password"
            }
        }

