from ast import Try
import numpy as np


# EJERCICIO 1

"""
    Dada una lista de nombre "listado" y con valores: 10,20,30,40,50
"""
# 1) Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"
# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)

listado = [10,20,30,40,50]

def inversaLista(lista):
    inverso = []                              
    for indice in range(-1,-len(lista)-1,-1):                     
        inverso.append(lista[indice])    

    return inverso


# EJERCICIO 2

"""
    Programa que coge por teclado 5 números y los almacena en una lista
    Nota:
    debería estar en la misma celda
    Hazlo como puedas, discurre cómo sería..
"""

def pedir_listado_teclado():
    lista = []

    for i in range(1, 6):

            lista.append(int(input("Escribe un número entero: ")))

            
    return lista

# EJERCICIO 3

"""
    Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay
    Nota: asume que son letras minúsculas sin tildes.
"""

# 1) Entrada de texto por teclado



# 2) Hazlo si puedes de varias formas
    # forma 1: contar vocales en palabra/frase


def cuenta_vocales(cadena):
    cont = 0 
    vocales = ["a", "e", "i", "o", "u","á", "é", "í", "ó", "ú"]
    for letra in cadena:
        if letra.lower() in vocales:
            cont+=1

    return cont



# 3) Hazlo de otra forma si se te ocurre..
    # forma 2

def cuenta_vocales2(cadena):
    cont = 0 
    for letra in cadena:
        if (letra.lower()=="a" or letra.lower()=="á") | (letra.lower()=="e" or letra.lower()=="é") | (letra.lower()=="i" or letra.lower()=="í") | (letra.lower()=="o" or letra.lower()=="ó") | (letra.lower()=="u" or letra.lower()=="ú"):
            cont+=1

    return cont


# EJERCICIO 4

"""
    Tablas de multiplicar:
    Haz algo tal que:
"""

# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>


# 2) Muestra los resultados de esta forma:

"""
    2 x 1 = 2
    2 x 2 = 4
    ...
    2 x 10 = 20
"""

def tabla_de_multiplicar(num):
    for numero in np.arange(0, 11):
        print(num, " x ", numero, " = ", num*numero)


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
        print("***** 4. EJERCICIO 4 **************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:  
                   
            listado = [10,20,30,40,50]

            print(inversaLista(listado))
            
            click=input("Press to continue...")
        elif opcion == 2: 
            
            print(pedir_listado_teclado())   
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            
            print(cuenta_vocales(input("Escribe una frase: ")))
            print(cuenta_vocales2(input("Escribe una frase: ")))

            click=input("Press to continue...")
        elif opcion == 4:   
            
            tabla_de_multiplicar(int(input("Elija número de la Tabla de multiplicar: 1 a 10: ")))
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")