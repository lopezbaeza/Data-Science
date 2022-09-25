import numpy as np
from time import sleep


# EJERCICIO 1

"""
    Dado: "np.arange(2,10)"
    sigue los siguientes pasos:
    1) Escribe esa instrucción y asígnaselo a la variable "a"
"""
def imprime(algo):
    print(algo)

# 2) ¿Es equivalente a "np.arange(2,10,1)"?


# 3) Se pide quedarse con aquellos números menores de 5.

    # hazlo con numpy si puedes para la variable "a"



# 4) Hazlo pasando esa información (de "a") a una lista


def menores5(array):
    menores=[]
    for elemento in array:
        if elemento<5:
            menores.append(elemento)
    return menores

# 5) En base a los resultados..

    # ¿Es posible recorrer 1 a 1 un array de numpy?


# 6) Haz el mismo proceso programando una sola línea (toma "a" como referencia)

def unaLinea(a):
    return [numero for numero in a if numero < 5]


# EJERCICIO 2

"""
    Para estos valores (v de valores por abreviar):
    v1 = 4
    v2 = 5
    v3 = 7
    v4 = 8
    El objetivo será calcular la media de estos valores
    Para ello sigue los siguientes pasos:
"""

# 1) Imprime los valores de esas variables v1,v2,v3,v4



# 2) Descomenta las 2 líneas siguientes para aprender..

    # que es posible asignar varios valores en la misma línea

    # Y la asignación de valores a variables se hace de forma consecutiva.

#3) Descomenta la línea siguiente para aprender una posible forma de calcular la media.

    #  Usamos nuevamente numpy..


# 4) Calcula la media sin usar numpy

    # Si el resultado no sale bien, razona cómo debería hacerse..

def media(v1,v2,v3,v4):
    return (v1 + v2 + v3 + v4) /4


# EJERCICIO 3

"""
    Factorial de un número
    Nota:
    El Factorial de 5, por ejemplo:
    5! = 5 * 4 * 3 * 2 * 1 = 120
    y el de 3:
    3! = 3 * 2 * 1 = 6
    y así para todos..
    PASOS A SEGUIR Y COSAS A TENER EN CUENTA
    Pide por teclado el número del cual quieres calcular el factorial.
    Para que no sea muy grande te recomendamos:
    3,4 o 5 (para hacer las pruebas)
    si ya no lo recuerdas o nunca lo viste, no te preocupes..
    3! es: 3 * 2 * 1 = 6
    4! es: 4 * 3 * 2 * 1 = 24
    5! es: 5 * 4 * 3 * 2 * 1 = 120
    (esto es lo que se pide, en esencia)
"""

def pide_numero():
    tirando=True
    while tirando:
        numero=int(input("Introduce un valor 3, 4 ó 5..."))
        if numero < 3 or numero > 5:
            print("....entre 3, 4 ó 5....")
            tirando=True
        else:
            tirando=False
            
    return numero

def factorial(numero):
    resultado=1
    for indice in range(1,numero+1):
        resultado=resultado*indice       
    
    return resultado

# EJERCICIO 4

"""
    Haz un cronómetro en Python:
    Obviamente:
    Horas - Minutos - Segundos
    Debes usar lo siguiente (from time import sleep)
    NOTA: Si quieres puedes usar sleep(0.000001)
    en vez de sleep(1) -> 1 segundo
    (para no esperar 1 segundo a ver los cambios)
    Para poder pararlo en poco tiempo,
    imprime mientras horas<2, cuando llegue a 2 debería parar la ejecución.
    Debería ejecutarse en unos 2 minutos aprox.
"""


def reloj(horas, minutos, segundos):
    print("h m s")
    for h in horas:
        for m in minutos:
            for s in segundos:
                if h<2:
                    print(h,m,s)
                    sleep(0.015)#Esto hace que los minutos sean como segundos, en total 2horas tarda 2mins
                    #sleep(0.000001)
                else:
                    break

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
            
            a=np.arange(2,10)
            imprime(a)
            # 2) ¿Es equivalente a "np.arange(2,10,1)"?
            a2=np.arange(2,10,1)
            imprime(a2)
            # 3) Se pide quedarse con aquellos números menores de 5.

                # hazlo con numpy si puedes para la variable "a"
            a3=np.arange(2,5)
            imprime(a3)
            
            click=input("Press to continue...")
            
            imprime(menores5(a2))
            
            click=input("Press to continue...")
            
            imprime(unaLinea(a))
            
        elif opcion == 2: 
            
            v1 = 4
            v2 = 5
            v3 = 7
            v4 = 8

            print(v1, v2, v3, v4)
            
            click=input("Press to continue...")
                   
            v1,v2,v3,v4 = 4, 5, 7, 8
            print(v1,v2,v3,v4)
            
            click=input("Press to continue...")
                    
            media_numpy = np.mean([v1,v2,v3,v4])

            imprime(media_numpy)            
            
            click=input("Press to continue...")
            
            imprime(media(v1,v2,v3,v4))
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            imprime(factorial(pide_numero()))
                
            click=input("Press to continue...")
        elif opcion == 4:     
            
            segundos=np.arange(0,60)
            minutos=np.arange(0,60)
            horas=np.arange(0,24)
            
            reloj(horas,minutos,segundos) 
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")