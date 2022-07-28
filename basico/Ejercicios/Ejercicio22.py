
import os
import settings

# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio 
    final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
    {
        "Producto":["Apio","Opio","Cebolla"],
        "Precio":[1000:,500,100],
        "Descuento":[20,10,12],
        "TipoDescuento":[apply_discount,apply_IVA,apply_IVA]
    }
"""

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
    Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, 
    y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA 
    a los productos de la cesta y devolver el precio final de la cesta.    
"""
def apply_discount(price, discount):
    # TODO: retorna precio  menos precio con descuento dividido entre 100
    return price - (price*discount/100)

def apply_IVA(price, percentage):
    # TODO: retorna el precio  suma precio por el porcentaje dividido por 100
    return price + (price*percentage/100)

def price_basket(basket, funcion):
    # TODO: retorna descuento o IVA
    lista_precios=list(basket.keys())
    lista_porcentajes=list(basket.values())
    total=0
    #mejor key,value in basket.items()
    for indice in range(len(basket)):
        total+=funcion(lista_precios[indice],lista_porcentajes[indice])
        
    return total  

# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""

def aplica_funcion_lista(funcion, lista):
    # TODO: recorrer la lista
    # TODO: apendizar los resultados de la función en una lista vacia
    # TODO: retorne la lista final
    resultado=[]
    
    for elemento in lista:
        resultado.append(funcion(elemento))
        
    return resultado

def cuadrado(n):
    # TODO: retorne n * n
    return pow(n,2)



# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""
def funcion_crea_diccionario(frase):
    palabras=frase.split()
    longitudes=[]
        
    for palabra in palabras:
        longitudes.append(len(palabra)) 
    #mejor así: 
    #longitudes=map(len,palabras)
    
    dicc = dict(zip(palabras, longitudes))
    
    return dicc
        
   
# EJERCICO 4

"""
    Escribir una función reciba una lista de notas y 
    devuelva la lista de calificaciones correspondientes a esas notas.
"""
def funcion_calificación(notas):
    calificaciones=[]
    for nota in notas:
        if nota<5:
            calificaciones.append("Supenso")
        elif nota >=5 and nota<6:
            calificaciones.append("Aprobado")
        elif nota >=6 and nota<7:
            calificaciones.append("Bien")
        elif nota >=7 and nota<8.5:
            calificaciones.append("Notable")
        elif nota >=8.5 and nota<=10:
            calificaciones.append("Sobresaliente")
        else: calificaciones.append("Nota errónea")
    
    return calificaciones

# EJERCICO 5

"""
    Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva 
    otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
"""

def fun_recalifica(dicc):
    lista_asignaturas=[]
    lista_notas=[]
    for key,value in dicc.items():
        lista_asignaturas.append(key.upper())
        lista_notas.append(value)
        
    lista_calificaciones=funcion_calificación(lista_notas)
        
    resutado  = dict(zip(lista_asignaturas, lista_calificaciones))
    
    return resutado   
     
# EJERCICO 6

"""
    Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
    pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
    por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def funcion_cosas_de_ficheros(fun):
    
    if fun==1:
        f = open(settings.MEDIA_ROOT + "password.txt", "r")
        linea=f.readline()
        f.close()
        
        return linea
    else:
        f = open(settings.MEDIA_ROOT + "password.txt", "a")
        print(f.write(input("Introduce Contraseña a almacenar: ")))
        f.close()
    
def fun_password(password):#password
    
    if password.lower()==funcion_cosas_de_ficheros(1).lower():
        print("Contraseña correcta, está ustéd validado")
        return True
    else: 
        print("Contraseña incorrecta, inténtelo de nuevo")
        return False
    
borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        print("\n")
        print("*************************** MENU **************************")
        print("************************ EJERCICIOS ***********************")
        print("***** 1. Descuentos, IVAs... ******************************")
        print("***** 2. Función a función... *****************************")
        print("***** 3. Recibe frase, devuelve lista con palabras y long *")        
        print("***** 4. Las notas! - Listas ******************************")
        print("***** 5. Las notas! - Diccionarios ************************")
        print("***** 6. Password *****************************************")
        print("***** 99. Salir (del menú) ********************************")
        print("***********************************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:   
            borrarPantalla()
            
            diccionario={1000:20, 500:10, 100:12}
            
            print(diccionario)
            print("Descuento")
            print(price_basket(diccionario, apply_discount))
            print("IVA")
            print(price_basket(diccionario, apply_IVA))
            print("Descuentos comprobación: ")
            print(apply_discount(1000, 20))
            print(apply_discount(500, 10))
            print(apply_discount(100, 12))
            
            print("IVAS comprobación: ")
            print(apply_IVA(1000, 20))
            print(apply_IVA(500, 10))
            print(apply_IVA(100, 12))
        elif opcion == 2: 
            borrarPantalla()
            
            listaentrada=[2,4,6,8,88,1,3,23]

            print(f"Lista inicial: {listaentrada} \n resulado: {aplica_funcion_lista(cuadrado,listaentrada)}")
        elif opcion == 3: 
            borrarPantalla() 
            
            print(funcion_crea_diccionario("Hola mundo"))
        elif opcion == 4:   
            borrarPantalla()
            
            lista_notas=[0,3,4.9,5.5,5,6,6.8,7.9,8.4,8.5,9,10,11]
            
            print(f"Lista inicial: {lista_notas} \n resulado: {funcion_calificación(lista_notas)}")
        elif opcion == 5: 
            borrarPantalla()
            
            diccionario_notas={"Matemáticas":8, "Ciencias Naturales":6,"Lenguaje":4,"Educación Física":8.6,"Física y Química":5.9,"Religión":3}
            
            print(f"Diccionario inicial: {diccionario_notas} \n resulado: {fun_recalifica(diccionario_notas)}")
            
        elif opcion == 6: 
            borrarPantalla()
            
            funcion_cosas_de_ficheros(2)
            
            while True:
                if fun_password(input("Introduce contraseña a comprobar: ")):
                    break
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()

print("Enhorabuena acabaste los ejercicios")