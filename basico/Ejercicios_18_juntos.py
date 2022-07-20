

# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""

def max(num1,num2):
    if num1==num2:
        return "Son iguales"
    elif num1>num2:
        return num1
    else: return num2
    
def pide_input(texto):
    while True:
        try:
            numero=int(input(texto))
            break
        except: print("Un número entero")
        
    return numero


print("EJERCICIO 1 - Mayor?")

x=pide_input("Introduce número...")
y=pide_input("Introduce número...")

print(f"El número mayor es {max(x,y)}")

# EJERCICIO 2

"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""

def max_de_tres(num1,num2,num3):
    if num1==num2==num3:
        return "Son iguales"
    elif num1>num2:
        if num1>num3:
            return num1
        else: return num3
    else: 
        if num2>num3:
            return num2
        else: return num3

def max_de_tres_v2(num1,num2,num3):
    L=[]
    L.append(num1)
    L.append(num2)
    L.append(num3)
    
    L.sort()
    return L[-1]
    
    

def pide_input(texto):
    while True:
        try:
            numero=int(input(texto))
            break
        except: print("Un número entero")
        
    return numero

print("EJERCICIO 2 mayor de tres")

x=pide_input("Introduce número...")
y=pide_input("Introduce número...")
z=pide_input("Introduce número...")

print(f"El número mayor es {max_de_tres(x,y,z)}")

print(f"El número mayor con fun2 es {max_de_tres_v2(x,y,z)}")

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

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


print("EJERCICIO 3 contar letras")

x=pide_input("Introduce Texto...")

cuenta_palabras(x)

print(f"El número de letras con fun 2 es {cuenta_palabras_v2(x)}")

lista=[3,5,8,0,1,234,546,789,2]
cuenta_palabras(lista)

print(f"El número de letras con fun 2 es {cuenta_palabras_v2(lista)}")

# EJERCICIO 4

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

print("EJERCICIO 4 Es vocal?")

x=pide_input("Introduce letra...").upper()

if saca_vocal(x):
    print("Si")
else:
    print("No")


# EJERCICIO 5

def sum(lista):
    suma=0
    for num in lista:
        suma=suma+num

    return suma

def multip(lista):
    multiplicacion=1
    for num in lista:
        multiplicacion=multiplicacion*num

    return multiplicacion

lista=[1,2,3,4]

print("EJERCICIO 5 suma y mult de ",lista)

print(f"La suma es {sum(lista)}")
print(f"La multiplicación  es {multip(lista)}")

print("Enhorabuena acabaste los ejercicios")