# Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt


# EJERCICIO 1

"""
    Escribe el código necesario en Python para:
    almacenar con una lista de nombre "clientes" los siguientes nombres:
    "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"
"""
def imprime(algo):
    print(algo)
    
def imprime_unoauno(lista):
    for cli in lista:
        print(cli)

clientes=["Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"]
imprime(clientes)

# 1) Para ese listado de clientes imprime todos ellos, 1 a 1
imprime_unoauno(clientes)
"""
    2) Dentro de ese grupo de clientes..
    se pide buscar..al cliente de nombre: "Juan García" si es posible
    Si lo encuentra, debería imprimir un mensaje tal que así:
    "el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes"
    Si no se le encuentra, debería salir un mensaje tal que así:
    "el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes"
    Nota: Comprueba en el caso de llevar o no acento
    Para:
    Juan García
    Juan Garcia
    Ojo con la tilde..
"""
def busca(lista):
    while True:
        cliente = input("Introduce un cliente: ")
        if cliente in lista:
            print(f"El cliente {cliente} SI se encuentra dentro de la \"BBDD\" de clientes")
            break
        else: 
            print(f"El cliente {cliente} NO se encuentra dentro de la \"BBDD\" de clientes, vuelva a intentarlo")
            continue
        
#busca(clientes)
"""
    3) Crea un DataFrame, de nombre df
    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)
    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,
            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González
    tarifas: 40,50,50,35,45,50,60,50,45
"""
tarifas=[40,50,50,35,45,50,60,50,45]

df = pd.DataFrame({"Clientes":clientes, "Tarifas":tarifas})
imprime(df)
# 4) Imprime las primeras 5 filas del DataFrame de 2 formas distintas

#forma1
imprime(df.head(5))
#forma2
def fun_5(df):
    for registros in range(0,5):
        for cols in range(0,df.shape[1]):
            print(df.iloc[registros,cols])
            
fun_5(df)
# 5) De ese DataFrame, selecciona solamente la columna "tarifas" e imprímela
    # (con 1 forma es suficiente, pero si sabes 2 mejor)
imprime(df[["Tarifas"]])
imprime(df.Tarifas)
# 6) Descomenta las siguientes líneas (algunos trucos y cosas útiles).
    # Ponlo en formato función!!

# df.tarifas.value_counts()

# df.tarifas.value_counts().plot(kind="bar")
# plt.show()

# df.tarifas.plot(kind="bar")
# plt.show

# print(df)


# 7) De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros (50 no incluído)
df_superior_50=df[df["Tarifas"]>50]
imprime(df_superior_50)


# EJERCICIO 2

# Número par o impar

# Prueba para los números 6 y 3

# Realiza un algortimo para saber si son pares o impares
def metenum():
    while True:
        try:
            numero=int(input("Introduce un número..."))
            break
        except:
            print("Vuelva a intentarlo...")
    return numero
def es_impar(numero):
    if numero==0:
        print(f"El valor {numero} es neutro")
    elif numero%2==0:
        print(f"El valor {numero} es PAR")
    else:
        print(f"El valor {numero} es IMPAR")

es_impar(metenum())

    # EJERCICIO 3

"""
    Intercambio de valores entre variables
    Siendo por ejemplo:
    x = 3 e y = 2
    Se pide hacer un pequeño algoritmo que me intercambie esos valores.
    Y que sea el resultado:
    x = 2 e y = 3
"""

# 1) Hazlo sin funciones
x=3
y=2

print(x,y)
aux=x
x=y
y=aux
print(x,y)
# 2) Hazlo mismo con una función

def funcion_switch (valor1,valor2):
    aux=valor1
    valor1=valor2
    valor2=aux
    
    return valor1,valor2

x=3
y=2
print(f"Antes de, el valor de X es {x} y el de Y es {y}")
print(f"Después de, el valor de X es {funcion_switch(x,y)[0]} y el de Y es {funcion_switch(x,y)[1]}")