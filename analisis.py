## Colegio Universitario de Cartago
## II Cuatrimestre 2025
## BIG DATA
## Programación II
## BD-132
## Tarea: Creaión API
## Nombre Docente: Osvaldo González Chavez
## Nombre Estudiante: Fabián Brenes Loría
## Carné: 303650023
## Fecha: 6-8-2025

import pandas as pd
from textblob import TextBlob

class AnalizadorSentimientos:
    def __init__(self, ruta_archivo, encoding='latin1', delimiter=';'):
        self.ruta_archivo = ruta_archivo
        self.encoding = encoding
        self.delimiter = delimiter
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        try:
            datos = pd.read_csv(self.ruta_archivo, encoding=self.encoding, delimiter=self.delimiter)
            print("Datos cargados correctamente:\n", datos)
            return datos
        except Exception as e:
            print("Error al cargar datos:", e)
            return pd.DataFrame()

    def obtener_sentimiento(self, texto):
        polaridad = TextBlob(str(texto)).sentiment.polarity
        if polaridad > 0.3:
            return "Positivo"
        elif polaridad < -0.3:
            return "Negativo"
        else:
            return "Neutro"

    def analizar(self, columna_texto="texto"):
        if columna_texto in self.datos.columns:
            self.datos["Sentimiento"] = self.datos[columna_texto].apply(self.obtener_sentimiento)
            print("Análisis de sentimientos completado:\n", self.datos)
        else:
            print(f"La columna '{columna_texto}' no existe en el DataFrame.")
        return self.datos

# Uso
analizador = AnalizadorSentimientos("comentarios.csv")
resultado = analizador.analizar()


