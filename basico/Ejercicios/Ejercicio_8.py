import pandas as pd
import numpy as np
import time

#EJERCICIO 1

# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1) Cadena de texto: hola como estas?

    # Nombre de la variable: "cadena"

# 2) Longitud de la cadena de texto


# 3) Longitud de la cadena de texto calculada con un bucle

def longitud(cadena):
    cont=0
    for letras in cadena:
        cont+=1
        
    print(f"La frase \"{cadena}\" tiene {cont} caracteres incluyendo espacios")


# EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6

def crea_dicc(Cursos, Notas):
    diccionario_notas={}

    cont=0
    for curso in Cursos:
        diccionario_notas[curso]=Notas[cont]
        cont+=1
        
    return diccionario_notas

def valores(dicc):
    return dicc.values()

def mediando(dicc):
    values=valores(dicc)
    return sum(values) / len(values)

# 1) Muestra el valor de las claves

def claves(dicc):
    return dicc.keys()

# 2) Muestra el valor de los valores del diccionario

# 3) Apendiza en el diccionario un nuevo elemento:

    # Machine Learning --> 9

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.

    # [["clave1", valor1], ["clave2", valor2]]

def listalista(dicci):
    lista_fin=[]
    for i,j in dicci.items():
        lista_aux=[]
        lista_aux.append(i)
        lista_aux.append(j)
        lista_fin.append(lista_aux)
    return lista_fin

# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta
def diccAdf(dicci):
    dfaux=pd.DataFrame(columns = ['Curso', 'Nota'])

    for i,j in dicci.items():
        dfaux[i]=j            
    return dfaux
def max_df(df):
    print(f"La nota mas alta es {df.max()}")
# 6) ¿y la nota más baja?

def min_df(df):
    print(f"La nota mas baja es {df.min()}")
# 7) Ordena el dataframe en orden descendente:

def ordena_df(df):
    return df.sort_values('Nota',ascending=False)

# EJERCICIO 3

"""
Dadas 2 funciones:
Determina cual de ellas ejecuta mas rápido.
Si sabes, hazlo de 2 formas.
función a
def main(): for i in range(10**8): pass
main()
función b
def main(): for i in np.arange(10**8): pass
main()
de 2 formas
"""
def main(): 
    for i in range(10**8): 
        pass
def main2(): 
    for i in np.arange(10**8): 
        pass
# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python

# 2) Escribe la matriz transpuesta.

    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.

def transponer(A):
    list_main = []
    for i in range(3):
        list_row = []
        for j in range(3):
            list_row.append(A[j][i])
        list_main.append(list_row)
    trans = np.array(list_main)
    return trans

import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def imprime(algo):
    print(algo)

def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("*************************** MENU **************************")
        print("************************ EJERCICIOS ***********************")
        print("***** 1. EJERCICIO 1 **************************************")
        print("***** 2. EJERCICIO 2 **************************************")
        print("***** 3. EJERCICIO 3 **************************************")
        print("***** 4. EJERCICIO 4 **************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            cadena="hola como estas?"
            imprime(cadena)
            
            imprime(len(cadena))

            longitud(cadena)
            
            click=input("Press to continue...")
        elif opcion == 2: 
            Cursos=["Python","Big Data","NLP"]
            Notas=[10,8,6]
            
            diccionario=crea_dicc(Cursos,Notas)
            
            imprime(diccionario)
            imprime(mediando(diccionario))
            
            click=input("Press to continue...")
        
            imprime(claves(diccionario))
                        
            click=input("Press to continue...")
        
            imprime(valores(diccionario))
            
            click=input("Press to continue...")
            
            diccionario["Machine Learning"]=9
            imprime(diccionario)
                        
            click=input("Press to continue...")
            
            imprime(listalista(diccionario))          
            
            click=input("Press to continue...")
            
            df=diccAdf(diccionario)
            imprime(df)      
            
            click=input("Press to continue...")
            
            max_df(df)
             
            click=input("Press to continue...")
            
            min_df(df)
             
            click=input("Press to continue...")
            
            imprime(ordena_df(df))
            
        elif opcion == 3: 
            
            a = time.time()
            main()
            b = time.time()

            tiempo = -a + b
            imprime(tiempo)
            
            click=input("Press to continue...")
            
            a = time.time()
            main2()
            b = time.time()

            tiempo = -a + b
            imprime(tiempo)
            
            click=input("Press to continue...")
        elif opcion == 4:     
             
            A = np.array([[1,2,3], [4,5,6], [7,8,9]])
            imprime(A)
             
            click=input("Press to continue...")
            
            A1 = np.arange(1,10)
            A=A1.reshape(3,3)
            imprime(A)
             
            click=input("Press to continue...")
            
            np.transpose(A)
             
            click=input("Press to continue...")
            
            A.T    
                
            click=input("Press to continue...")
            
            imprime(transponer(A))
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")