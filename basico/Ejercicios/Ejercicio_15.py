from optparse import Values
import pandas as pd
import numpy as np

# EJERCICIO 1


# 1) Crea una lista de nombre "Concursante" que contenga los siguientes valores:
    # "Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"
Concursante=["Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"]
# 2) Crea una lista de nombre "Resultados" que contenga los siguientes valores:
    # 20, 30, 50, 20, 10, 5, 60, 40
Resultado=[20, 30, 50, 20, 10, 5, 60, 40]
# 3) Crea un diccionario con los concursantes y los resultados.
dicc={'Concursante':Concursante, 'Resultado':Resultado}

#print(dicc.values())

# 4) Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for
def fun(dicci):
    df=pd.DataFrame(columns = ['Concursante', 'Resultado'])
    cont=0

    for i,j in dicci.items():
        print(i,j)
        df[i]=j

            
    return df


print(fun(dicc))
# 5) Con ayuda de loc filtra los resultados obtenidos desde Pedro hasta Lara.
df=fun(dicc)

#print(df
#df=fun(dicc)
df_filtro1=df.loc[1:5]
#print(df_filtro1)
# 6) Con ayuda de loc filtra los resultados obtenidos mayores o iguales a 40
df_filtro4=df.loc[df["Resultado"] >=40]
#print(df_filtro4)
# 7) Muestra el concursante con la mayor puntuación
df_filtro3=df.max()
#print(df_filtro3)
# 8) Muestra el concursante con la menor puntuación
df_filtro4=df.min()
#print(df_filtro4)
# 9) Modifica con la ayuda de loc los valores 20 por 0

df.loc[df["Resultado"]==20,"Resultado"]=0
#print(df)
# 10) Modifica Concursante "Juan" su puntuación por "None" con ayuda de .loc


df.loc[df["Concursante"]=="Juan","Resultado"]=None
print(df)

# EJERCICIO 2 (3)

"""
    Escribe un programa que pida dos palabras y diga si riman o no.
    Si coinciden las tres últimas letras tiene que decir que riman.
    Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""

def fun_pide_frase(texto):
    while True:
        try:
            palabra=str(input(texto))
            if(len(palabra)>3):
                break
            else:print("Más de 3 letras")
        except:
            print("Palabra")
    return palabra

def fun_caja_ritmos(palabra1,palabra2):
    if (palabra1[-2]==palabra2[-2]) and (palabra1[-1]==palabra2[-1]):
        if(palabra1[-3]==palabra2[-3]):
            print("RIMAN")
        else:print("RIMAN UN POCO")
    else:print("NO RIMAN NADA")

#fun_caja_ritmos(fun_pide_frase("Introduce la primera palabra: "),fun_pide_frase("Introduce la segunda palabra: "))