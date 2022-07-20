#4)Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

import numpy as np

def saca_vocal(texto):
    vocales=["A","E","I","O","U"]
    
    return texto in vocales 

def pide_input(texto):
    while True:
       entrada=input(texto)
       if len(entrada)>0:
            break
       else: print("Escribe algo")
        
    return entrada

x=pide_input("Introduce Texto...").upper()

if saca_vocal(x):
    print("Si")
else:
    print("No")