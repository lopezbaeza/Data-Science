# EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.
import numpy as np

# b) Apendiza un valor de valor 20, 32, 25, 32
def apendizar(lista1,lista2):
    for indice in range(0,len(lista1)):
        lista2.append(lista1[indice])
    return lista2

# c) Elimina el valor 8 de la lista
def elimina(lista,n):
    lista.remove(n)
    return lista
# d) Elimina los duplicados que haya en la lista test
def desduplicaYordena(lista):
    lista=list(set(lista))
    lista.sort()
    return lista
# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200

# f) ¿Cuántos valores se repiten entre las listas?
def repes(lista1,lista2):
    cont=0
    for indice in range(0,len(lista1)):
        if(lista1[indice] in lista2):
            print(lista1[indice])
            cont+=1
    print(f"Se repiten {cont} numeros")
# g) Muéstrame el maximo y mínimo en las dos listas

# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz

# i) Crea una función que se llame "funcion_división" donde se divida
    # el test con valor 32 entre info con valor 5 y muestra el resto de la división
def funcion_división (x,y):
    return x%y

def funcion_buscamultiplos(test1,info):
    for i in range(0,len(test1)):
        for j in range (0,len(info)):
            if (test1[i]==32 and info[j]==5):
                print(f"El resto de la división de {test1[i]} y {info[j]} es {funcion_división(test1[i],info[j])}")
# j) Con ayuda de reverse() muestra la inversa de test

# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"
def fun_creadicc(lista):
    newDict={}
    for indice_info in range(len(lista)):
        newDict[str(lista[indice_info][0])]=lista[indice_info][1]

    return newDict
# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"
def cambia(info2):
    for i in range (len(info2)):
        if(info2[i]==25):
            info2[i]="María"
        elif (info2[i]==20):
            info2[i]="Juan"
        elif(info2[i]==10):
            info2[i]="Pedro"
        
    return info2
# m) Sustituye en el listado test los multiplos de 2 por "Dos"
def cambia2(test1):
    for indice_test in range(len(test1)):
        if (test1[indice_test]%2==0):
            test1[indice_test]="Dos"
    return test1


# EJERCICIO 2

"""
    Escribe un programa que imprima los números desde 1 hasta 100
    Pero:
    * Para los múltiplos de 3 escribe "Hello"
    * Para los múltiplos de 5 escribe "World"
    * Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    (en vez de los números correspondientes)
"""
def fun_ejercicio2():
    for numero in range(1,101):
        if (numero%3==0 and numero%5==0):
            print("Hello World")
        elif numero%3==0:
            print("Hello")
        elif numero%5==0:
            print("World")
        else:
            print(numero)
        
import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("*************************** MENU ****************************")
        print("************************ EJERCICIOS *************************")
        print("***** 1. EJERCICIO 1 ****************************************")
        print("***** 2. EJERCICIO 2 ****************************************")
        print("***** 99. Salir (del menú) **********************************")
        print("*************************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            print("EJERCICIO 1.a")
            print("MODO 1")
            test1=[25, 8, 32, 20, 1]

            print(test1,type(test1))
            
            click=input("Press to continue...")        
            
            print("MODO 2")
            test2=list((25, 8, 32, 20, 1))

            print(test2,type(test2))
            
            click=input("Press to continue...")        
            
            print("MODO 3")
            test3=list(np.array((25, 8, 32, 20, 1)))

            print(test3,type(test3))
            
            click=input("Press to continue...")
            
            print("EJERCICIO 1.b")
            L1=[20, 32, 25, 32]            
            
            print(apendizar(L1,test1))
            
            click=input("Press to continue...")
            
            print("EJERCICIO 1.c")
            
            print(elimina(test1,8))
            
            click=input("Press to continue...")
            
            print("EJERCICIO 1.d")
            
            print(desduplicaYordena(test1))
            
            click=input("Press to continue...")
            
            print("EJERCICIO 1.e")
            
            info=[25, 100, 10, 20, 5, 25, 30, 200]
            print(info)
            
            
            click=input("Press to continue...")
            
            print("EJERCICIO 1.f")
            
            info=[25, 100, 10, 20, 5, 25, 30, 200]
            print(info)
            info.sort()
            print("Comparo ", info, " y ", test1)
            repes(test1,info)
                        
            click=input("Press to continue...")
            
            print("EJERCICIO 1.g")
            
            #test1
            print(min(test1), max(test1))
            
            #info
            print(min(info), max(info))
                        
            click=input("Press to continue...")
            
            print("EJERCICIO 1.h")
            
            print(test1)
            matriz=np.array(test1)
            print(matriz,type(matriz))
            
            click=input("Press to continue...")
            
            print("EJERCICIO 1.i")
            
            print(test1)
            print(info)
            funcion_buscamultiplos(test1,info)
                        
            click=input("Press to continue...")
                        
            print("EJERCICIO 1.j")
            
            print(test1)
            test1.reverse()
            print(test1)
                                    
            click=input("Press to continue...")
                        
            print("EJERCICIO 1.k")
            
            print(info)
            aux_info = list(enumerate(info))
            print(aux_info)
            print(fun_creadicc(aux_info),type(aux_info))
                                                
            click=input("Press to continue...")
                        
            print("EJERCICIO 1.l")
            
            info2=[25, 100, 10, 20, 5, 25, 30, 200]
            print(info2)
            print(cambia(info2))
                                                            
            click=input("Press to continue...")
                        
            print("EJERCICIO 1.m")
            
            print(test1)
            print(cambia2(test1))            
                                                            
            click=input("Press to continue...")
                        
        elif opcion == 2: 
            
            fun_ejercicio2()
            click=input("Press to continue...")

        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")