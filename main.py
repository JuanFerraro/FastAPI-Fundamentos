from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    }
]

""" End Point """
@app.get('/', tags=['Home']) 
def message():
    return HTMLResponse('<h1>Hola mundo</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies
