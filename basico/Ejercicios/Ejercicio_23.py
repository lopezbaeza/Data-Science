# Ejercicio 1

"""
    Desarrolla el siguiente ejercicios de POO:
   * Alumnos  -> Es la clase.
   * __init__ -> Es el método init
   * nombre, edad, asignatura y nota son las propiedades
   * Instanciamos..
   * los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
   * y el.__init__ los inicializa
   A continuación muestra la edad del alumno 2 y el alumno 3 y sus notas
"""
class Alumnos:
    def __init__(self,nombre, edad, asignatura,nota) -> None:
        self.nombre=nombre
        self.edad=edad
        self.asignatura=asignatura
        self.nota=nota


# Ejercicio 2

"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def fun_años_cumplidos(edad):
    for año in range(2022-edad,2022+1):
        print("Cumpliste en ",año)



# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
def fun_reves():
    palabra=input("Introduce una palabra: ")
    
    for letra in range(-1,-len(palabra)-1,-1):
        print(palabra[letra])
    
    print(palabra[::-1])
#con palabra[::-1] lo hace directamente
#
# Ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
def fun_nombre():
    
    nombre=input("Introduce tu nombre completo: ")
    
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.title())
       
#Hola

# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
def fun_telefono():
    
    while True:
        telefono=input("Introduce número teléfono completo, formato (+34-913724710-56): ")
        try:
            sin_prefijos=telefono.split("-")
            if len(sin_prefijos)>2:
                break
            else: 
                print("Formato (+34-913724710-56)")
        except:
            print("Formato (+34-913724710-56)")
            
    print(sin_prefijos[1])
       
#
# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

def fun_vocal_may():
    
    frase=input("Introduce frase: ")
    while True:
        vocal=input("Introduce vocal: ").lower()
        if vocal in ["a","e","i","o","u"]:
            break
        else:print("Vocal")
    nueva=""
    for letra in range(len(frase)):
        if frase[letra].lower()==vocal.lower():
            nueva+=vocal.upper()
        else: nueva+=frase[letra]
    #Mucho mejor frase.replace()
    print(nueva)
       
#
# Ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
def fun_leuros1():
    
    while True:
        try:
            leuros=float(input("Introduce precio con dos decimales: "))
            break
        except:print("Precio con dos decimales")
    
    decimal=round(leuros-(leuros//1),2)
    entero=leuros-decimal
            
    print(f"Precio: {entero} EUROS con {decimal} CÉNTIMOS")
    
def fun_leuros2():
        
    while True:
        try:
            leuros=input("Introduce precio con dos decimales: ").split(".")
            break
        except:print("Precio con dos decimales")  
        
    print(f"Precio: {leuros[0]} EUROS con {leuros[1]} CÉNTIMOS")

import math
     
def fun_leuros3():
        
    while True:
        try:
            leuros=float(input("Introduce precio con dos decimales: "))
            break
        except:print("Precio con dos decimales")
        
    parte_decimal, parte_entera = math.modf(leuros)
            
    print(f"Precio: {parte_entera} EUROS con {parte_decimal} CÉNTIMOS")
     

# Ejercicio 8

"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
    Mes Ventas Gastos
    Enero 30500 22000
    Febrero 35600 23400
    Marzo 28300 18100
    Abril 33900 20700
"""
import pandas as pd


def fun_crea_df():
    
    Mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    Ventas=[30500,35600,28300,33900,45500,8600,12300,33900,90500,4600,22300,50900]
    Gastos=[22000,23400,18100,20700,25500,4600,10300,38900,50500,2600,12300,70900]
    
    df=pd.DataFrame()
    
    df["Mes"]=Mes
    df["Ventas"]=Ventas
    df["Gastos"]=Gastos
    
    return df
  
#
# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""
def fun_balance(data,lista_meses):
    Balance=[]
    for mes in lista_meses:
        Balance.append(int(data[data["Mes"]==mes].Ventas-data[data["Mes"]==mes].Gastos))
  
    data["Balance"]=Balance
    
    return data

# Ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
"""
def fun_notas():
    asignaturas=["Matemáticas", "Ciencias Naturales","Lenguaje","Educación Física","Física y Química","Religión","Historia"]
    notas=[]
    
    for asigantura in asignaturas:
        notas.append(float(input(f"Introduce nota de {asigantura} ")))
        
    for asignatura in range(len(asignaturas)):
        print(f"Has sacado {asignaturas[asignatura]} la nota de {notas[asignatura]}")
    


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
        print("***** 4. EJERCICIO 4 **************************************")
        print("***** 5. EJERCICIO 5 **************************************")
        print("***** 6. EJERCICIO 6 **************************************")
        print("***** 7. EJERCICIO 7 **************************************")
        print("***** 8. EJERCICIO 8 **************************************")
        print("***** 9. EJERCICIO 9 **************************************")
        print("***** 10. EJERCICIO 10 ************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:         
            
            alumno1=Alumnos("Marciano",34,"Matemáticas",8.9)
            alumno2=Alumnos("Petra",22,"Física",5)
            alumno3=Alumnos("Francisco",40,"Circuitos",6)

            print("Edad de ",alumno2.nombre," es ", alumno2.edad)
            print("Nota de ",alumno2.nombre," es ", alumno2.nota)

            print("Edad de ",alumno3.nombre," es ", alumno3.edad)
            print("Nota de ",alumno3.nombre," es ", alumno3.nota)
            
            click=input("Press to continue...")
        elif opcion == 2: 
                             
            alumno1=Alumnos("Marciano",34,"Matemáticas",8.9)
            años=int(input("¿Edad? "))
            fun_años_cumplidos(años)
            print("----------")
            fun_años_cumplidos(alumno1.edad)
            
            click=input("Press to continue...")
        elif opcion == 3: 
            
            fun_reves()
            
            click=input("Press to continue...")
        elif opcion == 4:   
            
            fun_nombre() 
            
            click=input("Press to continue...")
        elif opcion == 5: 
            
            fun_telefono() 
            
            click=input("Press to continue...")
        elif opcion == 6: 
            
            fun_vocal_may()
            
            click=input("Press to continue...")
        elif opcion == 7:
            
            fun_leuros1()
            fun_leuros2()
            fun_leuros3()
            
            click=input("Press to continue...")
        elif opcion == 8: 
            
            print(fun_crea_df())
            
            click=input("Press to continue...")
        elif opcion == 9:
            
            Mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        
            print(fun_balance(fun_crea_df(),Mes))
            
            click=input("Press to continue...")
        elif opcion == 10: 
            
            fun_notas()
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")