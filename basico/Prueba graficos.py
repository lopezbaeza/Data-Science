import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=px.data.iris()
#df[df["sepal_length"]>2].plot(kind="bar")
df.plot(kind="line")
# lista_Columnas_a_relacionar=list(df.columns.values)

# print(lista_Columnas_a_relacionar)

# for columna in lista_Columnas_a_relacionar:
#      pd.crosstab(df[columna],df["species"]).plot(kind="bar")