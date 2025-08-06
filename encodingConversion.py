import pandas as pd

df = pd.read_csv("comentarios.csv", encoding="latin1", delimiter=";")
df.to_csv("comentarios_utf8.csv", encoding="utf-8", index=False)