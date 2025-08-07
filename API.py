from fastapi import FastAPI, UploadFile, File
import pandas as pd

from modelos.textblob_clase import AnalizadorSentimientos
from modelos.robertuito_clase import AnalizadorComentarios

app = FastAPI()

@app.post("/analisis-textblob/")
async def analizar_textblob(file: UploadFile = File(...)):
    df = pd.read_csv(file.file, encoding='latin1', delimiter=';')
    analizador = AnalizadorSentimientos("")
    analizador.datos = df
    resultado = analizador.analizar()
    return resultado.to_dict(orient="records")

@app.post("/analisis-robertuito/")
async def analizar_robertuito(file: UploadFile = File(...)):
    df = pd.read_csv(file.file, encoding='latin1', delimiter=';')
    analizador = AnalizadorComentarios("")
    analizador.datos = df
    analizador.procesar_sentimientos()
    return analizador.datos.to_dict(orient="records")