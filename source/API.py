import random

from fastapi import FastAPI

import main

app = FastAPI()

@app.get("/convert/{nombre}")
def convert(nombre):
    if nombre.isdigit() == False:
        nombre = random.randint(0,20)
    return {"nombre": int(nombre), "string":main.convertir(int(nombre))}

@app.get("/convert")
def convert():
    nombre = random.randint(0,999999999999)
    return {"nombre": int(nombre), "string":main.convertir(int(nombre))}

### uvicorn API:app --reload --host http://pedago.univ-avignon.fr --port 3247