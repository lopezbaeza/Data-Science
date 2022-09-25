##Versión rápida
#1)** Definir una función inversa() que calcule la inversión de una cadena. 
#Por ejemplo la cadena \"estoy probando\" debería devolver la cadena \"odnaborp yotse\""

import numpy as np
class Ejercicio1():
    def funcion_inversa(cadena):
        cadena_destino=""
        for letra in np.arange(-1,-len(cadena)-1,-1):
            cadena_destino=cadena_destino+cadena[letra]
        return cadena_destino

    def funcion_inversa2(cadena):
        return cadena[::-1]
    
    def pide_input(texto):
        while True:
            entrada=input(texto)
            if len(entrada)>0:
                    break
            else: print("Escribe algo")
        return entrada


#2)** Definir una función es_palindromo() que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo (\"radar\") tendría que devolver True."

class Ejercicio2:
    def es_palindromo1(cadena):    
        cadena_destino=Ejercicio1.funcion_inversa(cadena)
        
        if cadena==cadena_destino: return True
        else: return False

    def es_palindromo2(cadena):
        cont=0
        resultado=True
        
        for letra in np.arange(-1,-len(cadena)-1,-1):
            if cadena[letra]!=cadena[cont]:
                resultado=False
                break
            cont+=1
        return resultado
       
    def pide_input(texto):
        while True:
            entrada=input(texto)
            if len(entrada)>0:
                    break
            else: print("Escribe algo")
        return entrada
    

#3)** Definir una función superposicion() que tome dos listas y devuelva True 
# si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado."

class Ejercicio3:
    def superposicion(lista1,lista2):
        resultado=False
        
        for i in lista1:
            for j in lista2:
                if i==j:
                    resultado=True
                    break
        return resultado


import os
borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def funcion_menu():
    while True:
        
        borrarPantalla()
        print("\n")
        print("**************** MENU *******************")
        print("************** EJERCICIOS ***************")
        print("***** 1. Inversa de cadena **************")
        print("***** 2. Palíndromo *********************")
        print("***** 3. Superposición ******************")
        print("***** 99. Salir (del menú) **************")
        print("*****************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:
            
            texto=Ejercicio1.pide_input("Intrododuce una frase: ")
            print(f"Para la función 1: {Ejercicio1.funcion_inversa(texto)}")
            
            texto=Ejercicio1.pide_input("Intrododuce una frase: ")
            print(f"Para la función 2: {Ejercicio1.funcion_inversa(texto)}")
            
            click=input("Press to continue...")
        elif opcion == 2:
            
            palabra=Ejercicio2.pide_input("Intrododuce una palabra: ")
            
            print("Para la función 1:")
            if Ejercicio2.es_palindromo1(palabra):
                print(f" '{palabra}' SI es palíndromo")
            else: 
                print(f" '{palabra}' NO es palíndromo")

            print("Para la función 2:")
            if Ejercicio2.es_palindromo2(palabra):
                print(f" '{palabra}' SI es palíndromo")
            else: 
                    print(f" '{palabra}' NO es palíndromo")
                        
            click=input("Press to continue...")
        elif opcion == 3:
            
            l1=[1,2,3,4,5]
            l2=[6,7,8,9,10]
            l3=[5,11,12,13]

            print(l1,l2,Ejercicio3.superposicion(l1,l2))
            print(l2,l3,Ejercicio3.superposicion(l2,l3))
            print(l1,l3,Ejercicio3.superposicion(l1,l3))
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")