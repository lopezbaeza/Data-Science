import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# 1) Lee con pandas el archivo train.csv correspondiente al titanic dataset

df = pd.read_csv(".//media//train.csv")

# Descomentar para ejecutar:
#print(df)


"""
    2) Hacer un bucle for para automatizar las gráficas de pd.crosstab
    Se pide relacionar la columna Survived con Pclass, Sex y Embarked
    Nota:
    Se pide que dentro del bucle for se encuentre la gráfica requerida.
    Entonces, en una sola celda, tenemos 3 gráficas mostradas y todo automatizado.
"""

"""
    3) Hacer una función para automatizar las gráficas de pd.crosstab
    Se pide relacionar la columna Survived con Pclass, Sex y Embarked
    NOTA:
    Se pide definir una función (1 vez por ello)
    y hacer llamadas a la función (3 en este caso, para: Pclass, Sex, Embarked)
"""
def autom(lista_Columnas_a_relacionar):
    for columna in lista_Columnas_a_relacionar:
        pd.crosstab(df[columna],df["Survived"]).plot(kind="bar")
        plt.show()
        
Columnas_a_relacionar=["Sex","Embarked","Pclass"]

#autom(Columnas_a_relacionar)
# EJERCICIO 2

# Ejercicio de obtener los valores que muestra el pd.crosstab de Sex y Pclass sin usar el propio pd.crosstab
#print(pd.crosstab(df["Sex"],df["Pclass"]))

# 1) Imprime nuevamente los primeros 5 valores
df_duplica=df.loc[:,["Sex","Pclass"]].value_counts()
#print(df_duplica)
# 2) Usando value_counts() observa cuantos hombres y mujeres hay

    # (No hace falta plotear, simplemente mostrar los números de cada)

#print(df.Sex.value_counts())
# 3) Sin usar value_counts() observa cuantos hombres y mujeres hay (con un algoritmo)
def fun_contar_sexos(data,valor1,valor2):
    homb=0
    muj=0
    
    for persona in data[valor1]:
        if persona==valor2:
            homb+=1
        else:
            muj+=1
    return homb,muj
# print("(Hombres, Mujeres)")
# print(fun_contar_sexos(df,"Sex","male"))

"""
    4) Ahora haz lo mismo de otra forma
    En esta ocasión se pide que:
    crees un dataframe con el formato del original,
    bajo la permisa que sea un dataframe con todo hombres (primeramente) y con todo mujeres (a continuación)
    (2 DataFrames por tanto)
    Y observes si el número de filas de ambos nuevos DataFrames coincide con los valores anteriores
"""
def filtra_df(dataf,Ncolumna,Vcolumna):
    df_aux=dataf[dataf[Ncolumna]==Vcolumna]
    return df_aux

df_hombres=filtra_df(df,"Sex","male")
df_mujeres=filtra_df(df,"Sex","female")

# print("Hombres",df_hombres.describe())
# print("Mujeres",df_mujeres.describe())