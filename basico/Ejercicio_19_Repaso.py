#1)** Definir una función inversa() que calcule la inversión de una cadena. 
#Por ejemplo la cadena \"estoy probando\" debería devolver la cadena \"odnaborp yotse\""

import numpy as np

def funcion_inversa(cadena):
    cadena_destino=""
    for letra in np.arange(-1,-len(cadena)-1,-1):
         cadena_destino=cadena_destino+cadena[letra]
    return cadena_destino

def funcion_inversa2(cadena):
    return cadena[::-1]

texto="Hola dsqedqdes"
texto

print(funcion_inversa(texto))
print(funcion_inversa2(texto))
#2)** Definir una función es_palindromo() que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo (\"radar\") tendría que devolver True."

def es_palindromo1(cadena):    
    cadena_destino=funcion_inversa(cadena)
    
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

print("level")
print(es_palindromo1("level"))
print(es_palindromo2("level"))
print("radar")
print(es_palindromo1("radar"))
print(es_palindromo2("radar"))
print("ada")
print(es_palindromo1("ada"))
print(es_palindromo2("ada"))
print("qwadawq")
print(es_palindromo1("qwadawq"))
print(es_palindromo2("qwadawq"))
print("jamon")
print(es_palindromo1("jamon"))
print(es_palindromo2("jamon"))

#3)** Definir una función superposicion() que tome dos listas y devuelva True 
# si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado."

def superposicion(lista1,lista2):
    resultado=False
    
    for i in lista1:
        for j in lista2:
            if i==j:
                resultado=True
                break
    
    return resultado
                

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[5,11,12,13]

print(l1,l2,superposicion(l1,l2))
print(l2,l3,superposicion(l2,l3))
print(l1,l3,superposicion(l1,l3))