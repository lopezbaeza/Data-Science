#5)Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

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

print(f"La suma es {sum(lista)}")
print(f"La multiplicación  es {multip(lista)}")