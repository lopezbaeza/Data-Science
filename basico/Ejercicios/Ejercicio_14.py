
import pandas as pd

# EJERCICIO 1

"""
    Cada número es la suma de los 2 anteriores:
    0-1-1-2-3-5-8-13-21-34...
    Se pide programar esa secuencia con Python.
    Nota:
    Apendiza elementos hasta tener 10 primeros resultados.
    (los 10 números indicados desde 0 hasta 34)
    Si sabes, hazlo de varias formas diferentes
"""

def fibonacci():
    L = [0, 1]
    while (len(L) < 10):
        L.append(L[-1] + L[-2])
    return L

# print(fibonacci())



# EJERCICIO 2

# Cada número es la suma de los 2 anteriores:

# 0-1-1-2-3-5-8-13-21-34...

# Se pide programar para los números de fibonacci mayores de 1000
def fun_saca_fibonacci_desde_v1(listado_millon,x):
    listado_desde=[]

    for indice in range(0,len(listado_millon)):
        if listado_millon[indice]>=x:
            listado_desde.append(listado_millon[indice])
            
    return listado_desde
# Primero muestra los valores de 0 hasta 1000000, crea una lista
def fun_saca_fibonacci_hasta(x):
    cont=0
    fibos=[0,1]
    
    while True:
        nuevo_fibo=fibos[cont]+fibos[cont+1]
        if nuevo_fibo<x:
            fibos.append(nuevo_fibo)
            cont+=1
        else:break
    return fibos

# con ese listado crea una segunda lista con los mayores de 1000
def fun_saca_fibonacci_desde(listado_millon,x):
    listado_desde=[]

    for indice in range(0,len(listado_millon)):
        if listado_millon[indice]>=x:
            listado_desde.append(listado_millon[indice])
            
    return listado_desde

listado_con_millon=fun_saca_fibonacci_hasta(1000000)
print(listado_con_millon)
listado_desde_1000=fun_saca_fibonacci_desde(listado_con_millon,1000)
print(listado_desde_1000)

# EJERCICIO 3

# Se pide crear un NUEVO dataframe para cada uno de los siguientes casos

# planteados y que están relacionados con el Titanic DataSet

# (antes debéis de cargar el archivo como df)

# 1) Leer el archivo train.csv del titanic dataset

#df = pd.read_csv("./src/train.csv")

Barco=pd.read_csv(".\\media\\train.csv")
# Descomentar para ejecutar:
print(Barco)

# 2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven

    # NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado
def sobre():
    df_sobreviven=Barco[Barco.Survived==1]
    return df_sobreviven
print(sobre())
# 3) Crear un dataframe de nombre df__no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobrevive
df__no_sobreviven=Barco[Barco.Survived==1]
print(df__no_sobreviven)
# 4) DataFrame de hombres que no sobrevivieron en el titanic
df_hombres_no_sobreviven=Barco[(Barco.Survived==0) & (Barco.Sex=="male")]
print(df_hombres_no_sobreviven)
# 5) DataFrame de hombres que si sobrevivieron en el titanic
df_hombres_si_sobreviven=Barco[(Barco.Survived==1) & (Barco.Sex=="male")]
print(df_hombres_si_sobreviven)
# 6) DataFrame de mujeres que no sobrevivieron en el titanic
df_mu_no_sobreviven=Barco[(Barco.Survived==0) & (Barco.Sex=="female")]
print(df_hombres_no_sobreviven)
# 7) DataFrame de mujeres que si sobrevivieron en el titanic
df_mu_si_sobreviven=Barco[(Barco.Survived==1) & (Barco.Sex=="female")]
print(df_mu_si_sobreviven)