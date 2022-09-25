import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo
def imprimelistado(lista):
    return print(lista)



# 2) Prueba con min(listado)

def minimo(lista):
    return min(lista)


# 3) Realiza lo mismo pero con bucles y condicionales

# una opción...

def sacamin(lista):
    tam=len(lista)
    mini=lista[0]
    while tam>0:
        if (lista[tam-1]<mini):
            mini=lista[tam-1]
        tam=tam-1
    return mini

# otra opción...

def minimo_3(lista):
    minimo = 1000000

    for numero in lista:
        if numero < minimo:
            minimo = numero

    return minimo

# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# 2) Prueba con max(listado)

def maximo(lista):
    return max(lista)

# 3) Realiza lo mismo pero con bucles y condicionales

def sacamax(lista):
    maxi=lista[0]
    for elemento in lista:
        if elemento>maxi:
            maxi=elemento
    return maxi



# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo


# 2) Prueba a usar sort()

def colocar(lista):
    lista.sort(reverse=False)
    return lista

# 3) Realiza lo mismo pero con bucles y condicionales

# me creo una copia para no perder la información


def ordena(lista):
    listado_ascendente=[]
    while len(lista)>0:
        listado_ascendente.append(min(lista))
        lista.remove(min(lista))
    
    return listado_ascendente



# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo


# 2) Prueba a usar sort()

def colocar_3(lista):
    lista.sort(reverse=True)
    return lista

# 3) Realiza lo mismo pero con bucles y condicionales
def ordenaalreves(lista):
    listado_ascendente=[]
    while len(lista)>0:
        listado_ascendente.append(max(lista))
        lista.remove(max(lista))
    
    return listado_ascendente


# EJERCICIO 5
"""
    Escribe el código necesario en Python para:
    * almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:
    * Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.
"""
# 1) Para ese listado imprime todas ellas, 1 a 1

"""
    2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.
    y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.
    Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)
    Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)
    Imprime ese listado al terminar de almacenarlos.
"""


"""
    3) Crea un DataFrame, de nombre df con esa información en base
    a la siguiente relación de módulos y horas de clase módulos:
    Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP
    horas: 25, 15, 5, 15, 5, 10
"""

def imprimeunoauno(listado):
    for elemento in listado:
        print(elemento)

"""
    2) 
"""
def materiasesenciales(listado):
    esenciales=[]
    for elemento in listado:
        if elemento == "Python" or elemento == "Algoritmos":
            esenciales.append(elemento)
    return esenciales

"""
    3) 
"""
def imprimedf(data):
    print(data)

# 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela


# 5) Muestra el gráfico (plot) para la columna "horas"

# 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación

# 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación



# 8) De ese DataFrame, selecciona solamente (si fuera posible)
    # aquellas materias que tienen mas de 26 horas de dedicación


# 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

    # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia


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
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            listado=[30, 20, 10, 50, 40]

            imprimelistado(listado)

            print(minimo(listado))

            print(sacamin(listado))
            
            print(minimo_3(listado))
            
            click=input("Press to continue...")
        elif opcion == 2: 
            
            listado=[30, 20, 10, 50, 40]

            imprimelistado(listado)

            print(maximo(listado))
            
            print(sacamax(listado))
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            listado=[30, 20, 10, 50, 40]

            imprimelistado(listado)

            print(colocar(listado))
            # 3) Realiza lo mismo pero con bucles y condicionales

            listado=[30, 20, 10, 50, 40]
            print(ordena(listado))          
                
            click=input("Press to continue...")
        elif opcion == 4:     
                
            listado=[30, 20, 10, 50, 40]

            imprimelistado(listado)

            print(colocar_3(listado))

            listado=[30, 20, 10, 50, 40]
            print(ordenaalreves(listado))    
                
            click=input("Press to continue...")
        elif opcion == 5:     
                
            # 1) Para ese listado imprime todas ellas, 1 a 1
            modulos=["Big Data", "Python", "Algoritmos", "Machine Learning", "Deep Learning", "NLP"]

            imprimeunoauno(modulos)

            """
                2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.
                y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.
                Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)
                Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)
                Imprime ese listado al terminar de almacenarlos.
            """
   
                
            click=input("Press to continue...")
        
            imprimeunoauno(materiasesenciales(modulos))
            """
            3) Crea un DataFrame, de nombre df con esa información en base
                a la siguiente relación de módulos y horas de clase módulos:
                Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP
                horas: 25, 15, 5, 15, 5, 10
            """

            horas=[25, 15, 5, 15, 5, 10]

            df=pd.DataFrame({"Materias":modulos,"Horas":horas})

            imprimedf(df)   
                
            click=input("Press to continue...")
        
            # 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela

            dfh=df.Horas

            imprimedf(dfh)   
                
            click=input("Press to continue...")
        

            # 5) Muestra el gráfico (plot) para la columna "horas"
            df.Horas.plot(kind="bar")
            dfh.plot(kind="line")   
                
            click=input("Press to continue...")
        

            # 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación

            dfmas20=df[df.Horas>=20]

            imprimedf(dfmas20)   
                
            click=input("Press to continue...")
        

            # 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación

            dfmenos10=df[df.Horas<10]

            imprimedf(dfmenos10)   
                
            click=input("Press to continue...")
        

            # 8) De ese DataFrame, selecciona solamente (si fuera posible)
                # aquellas materias que tienen mas de 26 horas de dedicación
            dfmas26=df[df.Horas>26]

            imprimedf(dfmas26)   
                
            click=input("Press to continue...")
        
            # 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

                # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia
                
            df["Docente"]=["Enrique", "Susana", "Juan", "Ana", "Laura", "Patricia"]

            imprimedf(df)
                
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")