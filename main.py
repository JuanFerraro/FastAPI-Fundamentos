from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from database import connect_to_mongodb
from models import Movie

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

""" Conexion BD """
@app.on_event("startup")
async def startup():
    app.mongodb_client = connect_to_mongodb()

""" End Point """
@app.get('/', tags=['Home']) 
def message():
    return HTMLResponse('<h1>Hola mundo</h1>')

""" Ver todas las peliculas """
@app.get('/movies', tags=['movies'])
def get_movies():
    movies_collection = app.mongodb_client["movies"] #tomar la coleccion movies de la DB
    movies = movies_collection.find() #Utilizar busuqeda en mongoDB
    movie_list = []
    for movie in movies:
        movie["_id"] = str(movie["_id"])  # Convertir ObjectId a cadena
        movie_list.append(movie)
    return movie_list

""" Buscar movie por id """
@app.get('/movies/{id}', tags=['movies'])
def get_movie_by_id(id: int):
    movies_collection = app.mongodb_client["movies"]
    movie = movies_collection.find_one({"id": id})
    if movie:
        movie["_id"] = str(movie["_id"])  # Convertir ObjectId a cadena
        return movie
    else:
        raise HTTPException(status_code=404, detail="Película no encontrada")

""" Buscar película por categoria """
@app.get('/movies/categoria/{categoria}', tags=['movies'])
def get_movie_by_category(categoria: str):
    movies_collection = app.mongodb_client["movies"]
    movies = movies_collection.find({"categoria": categoria})  # Buscar películas por categoría
    movie_list = []
    for movie in movies:
        movie["_id"] = str(movie["_id"])
        movie_list.append(movie)
    
    if len(movie_list) == 0:
        raise HTTPException(status_code=404, detail="No se encontraron películas en la categoría especificada")
    
    return movie_list

""" Insertar nueva pelicula """
@app.post('/movies', tags=['movies'])
def add_movie(movie: Movie):
    movies_collection = app.mongodb_client["movies"]
    movie_dict = movie.dict()  # Convertir la instancia de Movie a un diccionario
    result = movies_collection.insert_one(movie_dict)
    if result.inserted_id:
        return {"message": "Película agregada correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al agregar la película")

