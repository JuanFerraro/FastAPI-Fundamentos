from fastapi import FastAPI

app = FastAPI()

""" End Point """
@app.get('/') 
def message():
    return "Hola Mundo!"