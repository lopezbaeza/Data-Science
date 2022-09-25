import pandas as pd
import numpy as np

# EJERCICIO 1

"""
    1) Haz un programa que calcule los múltiplos de 3
    Para ello primero debe preguntarse al usuario cuántos múltiplos desea añadir.
    Nota: Puedes usar un bucle while si lo deseas
"""
def multi():
    while True:
        try:
            numero=int(input("Número de multiplos de 3 a mostrar..."))
            break
        except:
            print("Introduce un número entero")
            
    lista=[]
    i=1
    while i<numero+1:
        print(f"Múltiplo de 3 número {i}: {i*3}")
        lista.append(i*3)
        i+=1
        
    return lista

  
# 2) Haz lo mismo con np.arange
def multiarr():
    while True:
        try:
            numero=int(input("Número de multiplos de 3 a mostrar..."))
            break
        except:
            print("Introduce un número entero")
       
    return np.arange(3,3*numero+1,3)

# EJERCICIO 2

"""
    Dado el listado del apartado 2
    Dada esta lista de variable "listado" y "valores": 10, 10, 20, 20, 20, 30, 40
    Se pide:
"""

# 1) Crea un DataFrame con esa información e imprímelo
def crea_df():
    listado=["l1","l2","l3","l4","l5","l6","l7"]
    valores=[10, 10, 20, 20, 20, 30, 40]

    dfaux=pd.DataFrame({"Listado":listado,"Valores":valores})

    return dfaux
# 2) Usa value_counts() para determinar cuántas repeticiones hay de cada número en esa columna


# 3) Haz un ".shape" a esa información del value_counts()

    # NOTA: Escribe: .shape justo al final

# 4) A esa misma instrucción con value_counts() escribe al final ".values"

    # Y veras la información..

    # pasa esa información a lista si puedes

    # y guarda ese listado como "repeticiones"


# 5) A esa información de value_counts() añade al final ".index"

    # Y pasa posteriormente a lista esa información

    # y guarda ese listado con el nombre: "valores"


# 6) Crea un DataFrame con 2 columnas,

    # 1 para "valores"

    # 1 para "repeticiones"

    # llámalo: "df_value_counts" (por ejemplo)

    # Y observa..


# 7) Haz lo siguiente: "df.value_counts()"

# 8) Observa si hay diferencias entre: "df" y "df_value_counts"



# EJERCICIO 3
"""
    Comparación de matrices
    Haz el código que testee si esas 2 matrices son iguales
    1)
    Dadas:
    matriz1 = np.array([[1,2],[3,4]])
    matriz2 = np.array([[1,2],[3,8]])
    PISTAS:
    -1- RECORRER MATRIZ1 Y MATRIZ2 CON LA PARAMETRIZACIÓN de i y j
    COMPROBAR: ( matriz1 [ i ][ j ] == matriz2 [ i ][ j ] )
    -2- crear una variable contador (inicializada en 0)
    y, cuando detecte, un número de una matriz en una posición concreta,
    y sea diferente del número que tiene LA OTRA MATRIZ..entonces..
    -3- incremento 1 unidad en dicho contador:
    SI los números son DISTINTOS
    --> entonces, que se incremente en 1 unidad..
    de tal manera que si ese contador=0 (al final)--> son todos iguales --> matriz1 = matriz2
    y si es distinto de 0 -> es que POR LO MENOS 1 vez encontró un número diferente
    matriz1 != matriz2
    -4- puedes usar np.arange( ) si lo deseas para las filas y para las columnas
    -5- recuerda el ejercicio del cronómetro para tener una referencia
"""
def funcion_compara(m1,m2):
    igual=0
    if m1.shape!=m2.shape:
        igual+=1
    else:
        for fila in range(0,m1.shape[1]):
            for columna in range(0,m2.shape[1]):
                print(m1[fila][columna],m2[fila][columna])
                if m1[fila][columna]==m2[fila][columna]:
                    continue
                else:
                    igual+=1
    return igual

import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("*************************** MENU **************************")
        print("************************ EJERCICIOS ***********************")
        print("***** 1. EJERCICIO 1 **************************************")
        print("***** 2. EJERCICIO 2 **************************************")
        print("***** 3. EJERCICIO 3 **************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            multi()  
            print(multiarr())
            
            click=input("Press to continue...")
        elif opcion == 2: 
                             
            df=crea_df()
            print(df)
            
            print(df.Valores.value_counts())
            print(df.Valores.value_counts().shape)
            print(df.Valores.value_counts().values)
            print(df.Valores.value_counts().index)
            
            valores2=list(df.valores.value_counts().index)
            print(valores2)
            repeticiones=list(df.value_counts().values)
            print(repeticiones)
            
            df_value_counts=pd.DataFrame({"valores":valores2,"repeticiones":repeticiones})
            print(df_value_counts)
            print(df_value_counts.value_counts())
            print(df.value_counts())
            print(df,df_value_counts)
            print(df.value_counts(),df_value_counts)
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            matriz1 = np.array([[1,2],[3,4]])
            matriz2 = np.array([[1,2],[3,8]])

            print(matriz1)
            print(matriz2)

            if funcion_compara(matriz1,matriz2):print("Son distintas")
            else:print("Son iguales")
            
            click=input("Press to continue...")
            
            matriz3 = np.array([[1,2],[3,4]])
            matriz4 = np.array([[1,2],[3,4]])
            
            print(matriz3)
            print(matriz4)
            
            click=input("Press to continue...")
            print(np.where(matriz3==matriz4,"Si","No"))
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")