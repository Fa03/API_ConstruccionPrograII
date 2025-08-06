#===============================================
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
#===============================================

# Imporación de librerías

import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string


modelo = "pysentimiento/robertuito-sentiment-analysis" # variable creada para asignar el modelo de sentimientos en español a usar

analizador = pipeline("sentiment-analysis",model = modelo) # carga el modelo de análisis de sentimientos (modelo pre-entrenado)

datos = pd.read_csv("comentarios1.csv", encoding='latin1', delimiter=";")
print(datos) # muestra los datos cargados

# Creación de función para anlizar los sentimientos de los comentarios

def analizarSentimiento (textoAnalizar):
    resultado = analizador(str(textoAnalizar))[0]
    return resultado["label"].lower()

datos["SentimientoGenerado"] = datos["texto"].apply(analizarSentimiento)
print(datos)

# =================== CREACIÓN DE GRÁFICO NUBE ====================================================

# Descarga stopwords en español
# nltk.download('stopwords')

texto_total = " ".join(str(comentario) for comentario in datos['texto'])

# Preparar palabras a excluir (stopwords + puntuación)
stop_words = set(stopwords.words('spanish'))
punctuacion = set(string.punctuation)

# Filtrar palabras: quitar stopwords y puntuación
palabras = [

    palabra.lower() for palabra in texto_total.split()

    if palabra.lower() not in stop_words and palabra not in punctuacion
]

# Unir nuevamente el texto limpio
texto_filtrado = " ".join(palabras)
# Crear la nube de palabras
nube = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(texto_filtrado)

# 8. Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(nube, interpolation='bilinear')
plt.axis("off")
plt.title("Nube de Palabras Más Frecuentes en Comentarios", fontsize=10)
plt.show()

# =================== CREACIÓN DE GRÁFICO DE BARRAS ====================================================

# Contar frecuencia de cada categoría
frecuencia = datos["SentimientoGenerado"].value_counts()
print(frecuencia) # mostar en pantalla la cantidad de veces que se presenta el valor

# Crear el gráfico de barras
plt.figure(figsize=(8, 5))
frecuencia.plot(kind="bar", color=["#FDE725", "#E2E418", "gray"])
plt.title("Frecuencia de Sentimientos Generados")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)  # Mantener etiquetas horizontales
plt.show()

# =================== CREACIÓN DE GRÁFICO DE CIRCULAR ====================================================

# Contar frecuencia de cada categoría
frecuencia = datos["SentimientoGenerado"].value_counts()

# Crear el gráfico circular
plt.figure(figsize=(7, 7))
plt.pie(frecuencia, labels=frecuencia.index, autopct="%1.1f%%", colors=["#FFA726", "#FFE0B2", "gray"])
plt.title("Proporción de Sentimientos Generados")
plt.show()
