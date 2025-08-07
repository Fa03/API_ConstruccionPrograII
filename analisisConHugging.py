import matplotlib.pyplot as plt
from transformers import pipeline
from wordcloud import WordCloud
from nltk.corpus import stopwords
import string
import pandas as pd

class AnalizadorComentarios:
    def __init__(self, ruta_csv, modelo="pysentimiento/robertuito-sentiment-analysis",
                 encoding="latin1", delimiter=";"):
        self.ruta_csv = ruta_csv
        self.encoding = encoding
        self.delimiter = delimiter
        self.modelo = modelo
        self.analizador = pipeline("sentiment-analysis", model=self.modelo)
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        try:
            datos = pd.read_csv(self.ruta_csv, encoding=self.encoding, delimiter=self.delimiter)
            print("Datos cargados:\n", datos)
            return datos
        except Exception as e:
            print("Error al cargar datos:", e)
            return pd.DataFrame()

    def _analizar_sentimiento(self, texto):
        resultado = self.analizador(str(texto))[0]
        return resultado["label"].lower()

    def procesar_sentimientos(self, columna_texto="texto"):
        if columna_texto in self.datos.columns:
            self.datos["SentimientoGenerado"] = self.datos[columna_texto].apply(self._analizar_sentimiento)
            print("Sentimientos generados:\n", self.datos)
        else:
            print(f"Columna '{columna_texto}' no encontrada.")
        return self.datos

    def generar_nube_palabras(self, columna_texto="texto"):
        texto_total = " ".join(str(comentario) for comentario in self.datos[columna_texto])
        stop_words = set(stopwords.words('spanish'))
        puntuacion = set(string.punctuation)

        palabras = [
            palabra.lower() for palabra in texto_total.split()
            if palabra.lower() not in stop_words and palabra not in puntuacion
        ]
        texto_filtrado = " ".join(palabras)

        nube = WordCloud(width=800, height=400, background_color='white',
                         colormap='viridis').generate(texto_filtrado)
        plt.figure(figsize=(10, 5))
        plt.imshow(nube, interpolation='bilinear')
        plt.axis("off")
        plt.title("Nube de Palabras Más Frecuentes en Comentarios", fontsize=10)
        plt.show()

    def grafico_barras(self):
        frecuencia = self.datos["SentimientoGenerado"].value_counts()
        print("Frecuencia de sentimientos:\n", frecuencia)
        plt.figure(figsize=(8, 5))
        frecuencia.plot(kind="bar", color=["#FDE725", "#E2E418", "gray"])
        plt.title("Frecuencia de Sentimientos Generados")
        plt.xlabel("Categoría")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=0)
        plt.show()

    def grafico_circular(self):
        frecuencia = self.datos["SentimientoGenerado"].value_counts()
        plt.figure(figsize=(7, 7))
        plt.pie(frecuencia, labels=frecuencia.index, autopct="%1.1f%%",
                colors=["#FFA726", "#FFE0B2", "gray"])
        plt.title("Proporción de Sentimientos Generados")
        plt.show()