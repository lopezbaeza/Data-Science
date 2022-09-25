# Ejercicio 1
# Se pide por tanto:
# -1- Leer el archivo train.csv de Titanic dataset con pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Barco=pd.read_csv("C:\\Users\\Matusaleno\\Documents\\Apuntes\\Curso Data Science\\Ejercicios\\Míos\\Dataset\\git_test\\Data-Science\media\\train.csv")
Barco=pd.read_csv(".\\media\\train.csv")

# -2- Imprimir algunas filas de la parte de arriba y otras de la parte del final
print(Barco.head(3))
print(Barco.tail(3))
# -3- Imprimir algunos parámetros estadísticos
Barco.plot(kind="bar")

plt.show()
# -4- Ver si en todas las columnas tenemos el mismo número de datos (solo verlo)
print(Barco.describe())
# -5- Ver el númers(o de hombres y mujeres que hay
print(Barco.Sex.value_counts())
# -6- Hacer alguna gráfica con pandas relativa al número de hombres y mujeres que hay
# Si quieres hacer alguna cosa más también puedes
# Necesitas descargar el train.csv subido al aula virtual en la parte de MATERIALES
# para la realización del ejercicio.

Barco.Sex.value_counts().plot(kind="bar")

plt.show()

# Ejercicio 2
# Dadas estas matrices:
# m1 = [[1, 10, 20], [30, 40, 50]]
# m2 = [[60, 80, 90,]]
# m3 = [[-2, 3, 5], [8, 6, 2]]
# 1)Comprueba si todos los valores de las matrices son mayores de 0
m1=np.array([[1, 10, 20], [30, 40, 50]])
m2=np.array([[60, 80, 90,]])
m3=np.array([[-2, 3, 5], [8, 6, 2]])
def enc_0(m):
    return np.where(m>0,"si","no")

print(enc_0(m1))
print(enc_0(m2))
print(enc_0(m3))
# 2)Si en la matriz m2 se encuentra el valor 80
np.where(m2==80,"AQUI","no")
np.any(m2==80)
# 3)Selecciona de m1 las dos últimas columnas
print(m1[:,1:3])
# 4)Concatena la m1 con m2, cuyo nombre de la matriz resultante sea m4
m4=np.concatenate((m1,m2),axis=0)
print(m4)
# 5)Convierte m1 y m3 en "np.matrix" asignando el nombre de matriz_1 y matriz_3, respectivamente
matriz_1=np.matrix(m1)
print(matriz_1)
matriz_3=np.matrix(m3)
print(matriz_3)
# 6)Realiza la resta, suma y producto de la matriz_1 y matriz_3
def suma(matriz_1,matriz_3):
    return matriz_1+matriz_3
def mult(matriz_1,matriz_3):
    return matriz_1*matriz_3.T
def resta(matriz_1,matriz_3):
    return matriz_1-matriz_3

print(suma(matriz_1,matriz_3))
print(mult(matriz_1,matriz_3))
print(resta(matriz_1,matriz_3))
# 7)Realiza las traza de la matriz de m4
print(m4.trace())
# Ejercicio 3

# Numeros Primos: Crear un listado de los numeros primos menores de 30
# Explicación inicial teórica
# (véase Tema_7..)
# Nota:
# si quieres apendiza el número 2,
# y a partir de ahí crea el algoritmo para apendizar los demas
# (menores de 30 en todo caso)
def fun_primos(x):
    cont=0
    
    for i in range(1,x+1):
        if(x%i==0):
            cont+=1
            
    return cont

def fun_comparar(x):
    if x==1 or fun_primos(x)==2:
        return True
    else:
        return False
    
def fun_carteles(x):
    if fun_comparar(x):
        print(f"{x} SI es primo")
    else:
        print(f"{x} NO es primo")
        
def fun_pedir_nummax():
    while True:
        try:
            x=int(input("Introduce número: "))
            break
        except:
            print("Número entero...")
    return x   
# 1)Pide por teclado un número
# Y di si es o no primo
# # solución
# # -> 4
numero=fun_pedir_nummax()

fun_carteles(numero)
# # -> 5
numero=fun_pedir_nummax()

fun_carteles(numero)
# 2)Escribe los números primos menores de 30
def fun_primos_menoresnum():
    primos_menoresnum=[]
    numero=fun_pedir_nummax()
    for i in range(numero,0,-1):
        if fun_comparar(i):primos_menoresnum.append(i)

    return primos_menoresnum

print(fun_primos_menoresnum())

# # solución
# 3)Numeros Primos: Crear un listado de los numeros primos menores de 200

print(fun_primos_menoresnum())
# # primos
# 4)Números Primos: Haz un listado de números primos entre 50 y 100
def primos_entre():
    primos_entre50_100=[]
    print("Número Mínimo")
    numero_min=fun_pedir_nummax()
    print("Número Máximo")
    numero_max=fun_pedir_nummax()
    for i in range(numero_max,numero_min-1,-1):
        if fun_comparar(i):primos_entre50_100.append(i)

    return primos_entre50_100

print(primos_entre())
# 5)Numeros Primos: Haz un listado de los 10 primeros números primos
# Si puedes hazlo de más de una forma, no necesario aun así


# # Solución (forma 1)
def fun1():
    primos_10=[]
    print("Número de primos a mostrar")
    numero=fun_pedir_nummax()
    contprimos=1
    indice=1

    while contprimos<numero+1:
        if fun_comparar(indice):
            primos_10.append(indice)
            contprimos+=1
        indice+=1
    return primos_10

# # if (0 not in listado_restos)
# #
# if (len(litado_restos)<10):
# #
# apendiza..

# # forma 2

def fun2():
    primos_10=[]
    print("Número de primos a mostrar")
    numero=fun_pedir_nummax()
    indice=1

    while True:
        if len(primos_10)<=numero-1:
            if fun_comparar(indice):
                primos_10.append(indice)
        else:break
            
        indice+=1
        
    return primos_10

print(fun1())
print(fun2())