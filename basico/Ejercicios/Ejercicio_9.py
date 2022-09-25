# EJERCICIO 1

"""
    Dado este listado de números:
    -3, 150, 0, 499, 500, 1200, -350, 0, 750, 25
    Haz un pequeño algoritmo que haga lo siguiente:
    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante
"""

# 1) Escribir en formato lista
Numeros=[-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]
# 2) Haz el propio ejercicio de programación planteado
def clasif(Lista):
    for numero in Lista:
        if numero<0:
            print("Negativo")
        elif numero==0:
            print("Cero - 0")
        elif numero>0 and numero<=200:
            print("Cero - 200")
        elif numero>200 and numero<500:
            print("200 - 500")
        elif numero==500:
            pass
        elif numero>500 and numero<1000:
            break
        else:
            print("Demasiado grande")
        
#clasif(Numeros)
# EJERCICIO 2

# Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40

# 1) Crea la lista e imprimela
listado=[10, 20, 20, 30, 40, 40, 40]

def imprime(lista):
    for elem in lista:
        print(elem)

#imprime(listado)
# 2) Haz un set de esa lista

#imprime(set(listado))
# 3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)

def buscaNOrep(lista):
    norepes=[]
    for elem in lista:
        if elem not in norepes:
            norepes.append(elem)
    return norepes

#imprime(buscaNOrep(listado))
# Pista: Puedes almacenar todo en una nueva lista



# EJERCICIO 3

# Dados estos clientes:

# Usando el continue/break

# Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

# 

clientes=["Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"]

def buscacliente(lista):
    while True:
        if input("Nombre: ") in lista:
            print("Está")
            break
        else: continue

buscacliente(clientes)
        