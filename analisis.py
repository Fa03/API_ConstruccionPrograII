## Colegio Universitario de Cartago
## II Cuatrimestre 2025
## BIG DATA
## Programación II
## BD-132
## Primer Examen
## Nombre Docente: Osvaldo González Chavez
## Nombre Estudiante: Fabián Brenes Loría
## Carné: 303650023
## Fecha: 10-6-2025

import pandas as pd
from textblob import TextBlob

datos = pd.read_csv("comentarios.csv", encoding='latin1', delimiter=";")
print(datos) # Muestra los datos del archivo csv

# Análisis de sentimientos

def obtenerSentimiento (textoAnalizar):
    rango = TextBlob(str(textoAnalizar)).sentiment.polarity

    #Clasificación
    if rango > 0.3:
        return "Positivo"
    elif rango < -0.3:
        return "Negativo"
    else: 
        return "Neutro"

datos["Sentimiento"] = datos["texto"].apply(obtenerSentimiento)
print(datos)




