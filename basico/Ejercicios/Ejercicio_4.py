# EJERCICIO 1

"""
    Crear un pequeño programa que calcule la multiplicación de 2 números (x, y)
    x = 3, y = 5
    x = 7, y = 3
"""

# a) Con una función (por ejemplo funcion_multiplicar)


def funcion_multiplicar(x, y):
    return x * y



# b) Con la función lambda (Tal vez puedes ir a repasarlo)


# otra opción...
def funcion_lambda(x, y):
    return (lambda x, y: x * y)(x, y)



# c) Realizarlo con entrada de teclado (input)

def funcion_input():
    return int(input("Introduce valor...: "))




# EJERCICIO 2

"""
    -A-
        Dado un string:
        "Level"
        ¿Es un palíndromo?
"""

def palindromo(cadena1):
    cadena2=""
    rango = range(len(cadena1)-1,-1,-1)
    for letra in rango:
        cadena2=cadena2+cadena1[letra]
        
    rango2=range(0,len(cadena1),1)
    palin="SI"
    for letra2 in rango2:
        if cadena1[letra2]!=cadena2[letra2]:
            palin="NO"

    print(f"{palin} son palíndromos : {cadena1} y {cadena2}")             
    return palin

"""
    -B-
        ¿Y este string?
        "level"
        Nota: "Es un palíndromo si se invierte el orden del string, el resultado es exactamente el mismo"
"""



# EJERCICIO 3

"""
    Dado 2 strings:
    S1 = "Hi!"
    S2 = "Hello!"
    Imprimir las letras que son comunes
"""

# Primera Opción

def iguales(S1, S2):
    iguales=[]
    letra=0;
    while letra<len(S1):
        if (S1[letra] in S2):
            iguales.append(S1[letra])   
        letra+=1;

    #Quito duplicados 
    pre_resultado=set(iguales)
    return list(pre_resultado)
    
def comunes(S1, S2):
    list_letras = []
    for elemento in S1:
        for letra in S2:
            if elemento == letra:
                list_letras.append(elemento)
    return list_letras

# print(comunes(S1, S2))

# Segunda opción...

def comunes_2(S1, S2):
    list_letras = []
    for elemento in S1:
        if elemento in S2:
            list_letras.append(elemento)
    return list_letras

# print(comunes_2(S1, S2))

# Tercera opción...

def comunes_3(S1, S2):
    sin_coincidencia = []
    for elemento in S1:
        for letra in S2:
            if elemento == letra and elemento not in sin_coincidencia:
                sin_coincidencia.append(elemento)
    return sin_coincidencia

# print(comunes_3(S1, S2))


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
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            print(funcion_multiplicar(3, 5))
            print(funcion_multiplicar(7, 3))
            
            resultado1 = (lambda x, y: x * y)(3, 5)
            resultado2 = (lambda x, y: x * y)(7, 3)
            print(resultado1)
            print(resultado2)
            # otra opción...
            # MEJOR OPCIÓN!!
            f = lambda x, y: x * y
            print(f(3, 5))
            print(f(7, 3))

            print(funcion_lambda(3, 5))
            print(funcion_lambda(7, 3))     
            
            x=funcion_input()
            y=funcion_input()

            print(funcion_multiplicar(x, y))
            
            click=input("Press to continue...")
        elif opcion == 2: 
            
            cadena="Level"
            
            print(palindromo(cadena))
            
            cadena="level"
            
            print(palindromo(cadena))
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            S1="Holla!" 
            S2="Hello!" 
            
            Lista_resultado=iguales(S1,S2)     
            
            print(S1)
            print(S2)
            print(Lista_resultado)   
                
            click=input("Press to continue...")
    
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")