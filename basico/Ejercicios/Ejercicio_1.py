import pandas as pd


# EJERCICIO 1

"""
    Decribe una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""


def imprime(algo):
    print(algo)

# EJERCICIO 2

"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""
def imprimir(s, y):
    print(f'El valor de s es {s} y el valor de y es {y}')
    print('El valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
    print('El valor de s es ', s, ' y el valor de y es ', y)
    print(f'El valor de s es %s y el valor de y es %s' %(s, y))
    print(f'El valor de "s" es %s y el valor de "y" es %s' %(s, y))
    print(f"El valor de \"s\" es {s} y el valor de \"y\" es {y}")


# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

def concatenar(name1, name2):
    resulta = name1 + " " + name2
    return resulta

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

def titulo(lafrase):
    return lafrase.title()

def mayusculas(lafrase):
    return lafrase.upper()

def minusculas(lafrase):
    return lafrase.lower()



# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""

def sumaValores(x, y):
    return x + y

def multiplicación(x, y):
    return x * y

def operación():
    return (2 + 32 * 10)

def elevado(x, y):
    result = x ** y
    return result

def redondeo(valor):
    return round(valor, 2)

def tipo(valor):
    return type(valor)

# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""

def absoluto(x):
    return  abs(x)

def maxmin(lista):
    print("máximo: ", max(lista))
    print("mínimo: ", min(lista))

# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""


def f8_1(lista):
    lista[1] = -1
    lista[-2] = -1
    return lista

def f8_2(lista):
    df = pd.DataFrame(lista, columns=["listado"])
    return df


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
        print("***** 5. EJERCICIO 5 **************************************")
        print("***** 6. EJERCICIO 6 **************************************")
        print("***** 7. EJERCICIO 7 **************************************")
        print("***** 8. EJERCICIO 8 **************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            notas = -3

            imprime(notas)
            
            click=input("Press to continue...")
        elif opcion == 2: 
                             
            s = 25
            y = 10

            imprimir(s, y)
  
            click=input("Press to continue...")
        elif opcion == 3: 
            
            name="Juan \"El profesor\""

            imprime(name)
            
            click=input("Press to continue...")
        elif opcion == 4:   
            
            imprime(concatenar("Juan", '"El profesor"'))
      
            click=input("Press to continue...")
        elif opcion == 5: 
            
            frase = "no cuentes los días, haz que los días cuenten"
            imprime(titulo(frase))
            imprime(mayusculas(frase))
            imprime(minusculas(frase))
            
            click=input("Press to continue...")
        elif opcion == 6: 
            x = 26
            y = 35
            imprime(sumaValores(x, y))
            imprime(multiplicación(x, y))
            imprime(operación())
            imprime(elevado(3, 9))
            imprime(redondeo(elevado(3, 9)))
            imprime(tipo(elevado(3, 9)))
            
            click=input("Press to continue...")
        elif opcion == 7:
            
            num = -32
            lista = [3, -6, 4, -10, 2.6666]

            imprime("Valor absoluto: " + str(absoluto(num)))
            maxmin(lista)
            
            click=input("Press to continue...")
        elif opcion == 8:
            
            L = [10, None, 8, 5, None, 20]
            imprime(f8_1(L))
            L = [10, None, 8, 5, None, 20]
            imprime(f8_2(L))
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")