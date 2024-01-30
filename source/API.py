import random

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import main

app = FastAPI()

@app.get("/convert/{nombre}")
def convert(nombre):
    if nombre.isdigit() == False:
        nombre = random.randint(0,20)
    return {"nombre": int(nombre), "string":main.convertir(int(nombre))}

@app.get("/rpg", response_class=HTMLResponse)
def rpg():
    content = open('./site/connexion.html', encoding="utf8").read()
    return HTMLResponse(content=content, status_code=200)

@app.get("/style.css", response_class=HTMLResponse)
def style():
    content = open('./site/style.css').read()
    return HTMLResponse(content=content, status_code=200)

### uvicorn API:app --reload --host http://pedago.univ-avignon.fr --port 3247