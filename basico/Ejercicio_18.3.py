#3)Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, 
# pero escribirla por nosotros mismos resulta un muy buen ejercicio.
import numpy as np

def cuenta_palabras(texto):
    cont=0
    for letra in texto:
        cont+=1
        print(f"Letra {letra} -> {cont}")
        
def cuenta_palabras_v2(texto):
    cont=0
    for letra in texto:
        cont+=1
    return cont

def pide_input(texto):
    while True:
       entrada=input(texto)
       if len(entrada)>0:
            break
       else: print("Escribe algo")
        
    return entrada

x=pide_input("Introduce Texto...")

cuenta_palabras(x)

print(f"El número de letras con fun 2 es {cuenta_palabras_v2(x)}")

lista=[3,5,8,0,1,234,546,789,2]
cuenta_palabras(lista)

print(f"El número de letras con fun 2 es {cuenta_palabras_v2(lista)}")