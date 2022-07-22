# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""
class Ejercicio1:
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

    def fun_ejercicio1():
        print("EJERCICIO 1 - Mayor?")

        x=Ejercicio1.pide_input("Introduce número...")
        y=Ejercicio1.pide_input("Introduce número...")

        print(f"El número mayor es {Ejercicio1.max(x,y)}")

# EJERCICIO 2

"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""
class Ejercicio2:
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

    def fun_ejercicio2():
        print("EJERCICIO 2 mayor de tres")

        x=Ejercicio2.pide_input("Introduce número...")
        y=Ejercicio2.pide_input("Introduce número...")
        z=Ejercicio2.pide_input("Introduce número...")

        print(f"El número mayor es {Ejercicio2.max_de_tres(x,y,z)}")

        print(f"El número mayor con fun2 es {Ejercicio2.max_de_tres_v2(x,y,z)}")

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
class Ejercicio3:
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

    def fun_ejercicio3():
        print("EJERCICIO 3 contar letras")

        x=Ejercicio3.pide_input("Introduce Texto...")

        Ejercicio3.cuenta_palabras(x)

        print(f"El número de letras con fun 2 es {Ejercicio3.cuenta_palabras_v2(x)}")

        lista=[3,5,8,0,1,234,546,789,2]
        Ejercicio3.cuenta_palabras(lista)

        print(f"El número de letras con fun 2 es {Ejercicio3.cuenta_palabras_v2(lista)}")

# EJERCICIO 4
class Ejercicio4:
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

    def fun_ejercicio4():
        
        print("EJERCICIO 4 Es vocal?")

        x=Ejercicio4.pide_input("Introduce letra...").upper()

        if Ejercicio4.saca_vocal(x):
            print("Si")
        else:
            print("No")


# EJERCICIO 5
class Ejercicio5:
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

    def fun_ejercicio5():
        lista=[1,2,3,4]

        print("EJERCICIO 5 suma y mult de ",lista)

        print(f"La suma es {Ejercicio5.sum(lista)}")
        print(f"La multiplicación  es {Ejercicio5.multip(lista)}")

def funcion_menu():
    while True:
        print("\n")
        print("**************** MENU *******************")
        print("************** EJERCICIOS ***************")
        print("***** 1. Mayor entre dos números ********")
        print("***** 2. Mayor entre tres números *******")
        print("***** 3. Longitud de un texto ***********")
        print("***** 4. Es vocal ?? ********************")
        print("***** 5. Suma y Multiplicación de lista *")
        print("***** 99. Salir (del menú) **************")
        print("*****************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:
            Ejercicio1.fun_ejercicio1()
        elif opcion == 2:
            Ejercicio2.fun_ejercicio2()
        elif opcion == 3:
            Ejercicio3.fun_ejercicio3()
        elif opcion == 4:
            Ejercicio4.fun_ejercicio4()
        elif opcion == 5:
            Ejercicio5.fun_ejercicio5()
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")