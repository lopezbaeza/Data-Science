import pandas as pd

# EJERCICIO 1

"""
   Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].
    Modifica con un algoritmo ese listado.
    Cuando encuentre Python debe poner un 1
    y cuando encuentre otro lenguaje de programacion, un 0
    es un simple ejemplo de modificación de valores en una lista.
"""

def transformacion(lista):
    for i in range(len(lista)):
        if lista[i] == "Python":
            lista[i] = 1
        else:
            lista[i] = 0
    return lista


# EJERCICIO 2

"""
    Dada la siguiente lista:
    L = [10, None, 8, 5, None, 20]
"""


# 1) Susitituir por -1 el valor None usando bucles y listas

def cambiar(lista):
    for i in range(0, len(lista)):
        if lista[i] == None:
            lista[i] = -1
    return lista


# 2) Creamos un dataframe con los valores de la lista y
#     modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)
def creadf(lista):
    df = pd.DataFrame(lista, columns=["Listado"])
    print(df)
    return df

def modificardf1(dfl):
    dfl.Listado = dfl.Listado.fillna(-1)
    return dfl

def modificardf2(dfl):
    dfl.loc[dfl["Listado"] == None , "Listado"] = -1
    return dfl

def modificardf3(dfl):
    dfl.loc[dfl["Listado"] == None , "Listado"] = -1
    return dfl


# 3) Vuelve a escribir el listado con falta de valores (inicial),
#     y sustituye por la media.

def modificardf4(dfl):
    dfl.Listado = dfl.Listado.fillna(dfl.Listado.mean())
    return dfl

# 4) Apendiza la columna con estos valores
def añadircolumna(dfl, lista2):
    dfl['Listado2'] = lista2
    return dfl

# 5) Elimina la columna L

def eliminarcolumna(dfl):
    dfl = dfl.drop(["Listado2"], axis=1)
    return dfl


# EJERCICIO 3

"""
    Crear un listado con los siguientes numeros:
        10, 20, 30, 40 (nombra la lista con nombre: "listado")
"""


# 1) Crea el listado e imprimelo:



# 2) Apendiza el valor 50 ( si es posible)

def añadirvalor(listado, numero):
    listado.append(numero)
    return listado


# 3) Modifica (si es posible) el valor 10 por 100

def modificavalor(listado, numero):
    listado[0] = numero
    return listado

# EJERCICIO 4

"""
    Dada una lista de nombre "Temperatura" con valores: 10, 20, 30, 40, 50
"""


# 1) Crea el listado e imprimelo:


# 2) En este "Temperatura". ¿Cuál es el elemento en la posición (index) 1?

def valorposicion(lista, posicion):
    return lista[posicion]


# 3) ¿Y en la posición (index) 0?


# 4) ¿Y en la posición (index) -1?



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
                   
            listado =  ["Python", "Matlab", "R", "VBA", "Julia", "C++"]
            print(listado)
            print(transformacion(listado))
            
            click=input("Press to continue...")
        elif opcion == 2: 
                             
            L = [10, None, 8, 5, None, 20]
            print(L)
            print(cambiar(L))
  
            click=input("Press to continue...")
            borrarPantalla()
            
            L = [10, None, 8, 5, None, 20]
            print(L)
            df=creadf(L)
            print(modificardf1(df))
            
            
            L = [10, None, 8, 5, None, 20]
            print(L)
            df=creadf(L)
            print(modificardf4(df))
            
            click=input("Press to continue...")
            borrarPantalla()
            
            L = [10, None, 8, 5, None, 20]
            print(L)
            df=creadf(L)
            listado2 = [10, 20, 50, 30, 20, 0]

            print(añadircolumna(df,listado2))
            
            click=input("Press to continue...")
            borrarPantalla()
  
            print(eliminarcolumna(df))
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            listado = [10, 20, 30, 40]
            print(listado)
            
            listado2 = añadirvalor(listado, 50)
            print(listado2)
            
            
            click=input("Press to continue...")
            borrarPantalla()
  
            print(modificavalor(listado2, 100))

            click=input("Press to continue...")
        elif opcion == 4:   
            
            Temperatura = [10, 20, 30, 40, 50]
            print(Temperatura)
            
            print("Posición 1: ",valorposicion(Temperatura, 1))
            
            

            print("Posición 0: ",valorposicion(Temperatura, 0))            
            
            
            print("Posición -1: ",valorposicion(Temperatura, -1))
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")