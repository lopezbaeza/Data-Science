"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1
print("------------------------------------")
"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    # TODO: tome un entero n
    # TODO: devuelva el caracter multiplicado por n
    frase=""
    while n>0:
        frase=frase+caracter
        #frase +=caracter
        n-=1
    return frase

car="w"
veces=7
print(f"Entrada {car} {veces} veces")
print(generar_n_caracteres(veces,car))

# EJERCICIO 2
print("------------------------------------")
"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
                "****"
                "*********"
                "*******"
"""

def procedimiento(lista):
    # TODO: tome una lista de numeros enteros
    # TODO: imprimir en la pantalla:

    # XXXX
    # XXXXXXXXX
    # XXXXXXX
    acum=""
    for elemento in lista:
        for i in range(elemento):
            acum=acum+"*"
            
        print(acum)
        acum=""

lista=[4,9,2]

print("Entrada ",lista)
procedimiento(lista)

# EJERCICIO 3
print("------------------------------------")
"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(lista):
    # TODO: tome una lista de palabras
    # TODO: devolver la más larga
    
    masalta=""
    for elemento in lista:
        if len(masalta)<len(elemento):
            masalta=elemento
    
    return masalta

lista=["Benemérita","Torquemada","Benalmádena","Sabiñánigo","Nicomedes","Ataúlfo","Perogrullo",
       "Botarate","Barbitúrico","Arcoseno","Circunloquio","Atapuerca","Sopicaldo","Panacea","Condolencia"
       ]

print(lista)
print("la palabra más larga es ",mas_larga(lista))

# EJERCICIO 4
print("------------------------------------")
"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    # TODO: tome una lista de palabras y un entero n
    # TODO: devolver las palabras que tengan n caracteres
    lista_result=[]
    for palabra in lista:
        if len(palabra)>n:
            lista_result.append(palabra)
    return lista_result


veces=8
print(f"Entrada máx de {veces} caracteres en {lista}")
print(filtrar_palabras(lista,veces))

# EJERCICIO 5
print("------------------------------------")
"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def c_mayusculas(cadena):
    # TODO: ingrese una cadena de texto
    # TODO:evaluar la cadena
    # TODO: returnar cuantas letras mayúsculas tiene
    cont_may=0;
    cont_min=0;
    cadena2=""
    cadena2.islower()
    for letra in range(len(cadena)):
        if cadena[letra].isupper():
            cont_may+=1
        else:cont_min+=1
    return cont_may, cont_min

texto="CircunloquioEscalopeMerendola"
mayusculas, minusculas = c_mayusculas(texto)
print("Palabra ",texto)
print("Número de mayúsculas ",mayusculas)
print("Número de minúsculas ",minusculas)
print(len(texto))

# EJERCICIO 6
print("------------------------------------")
"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

def mayores(tup):
    # TODO: definir una tupla de 10 edades de personas
    # TODO: imprimir la cantidad de personas con edades superiores a 20
    cont=0
    cont
    lista=[]    
    while cont<len(tup):
        if tup[cont]>20:
            print(tup[cont])
            lista.append(tup[cont])
        cont+=1
    return lista    
tupla=(21,34,92,1,22,19,5,9,13,67)

print(f"Entrada {tupla} sacar los mayores de 20")
print(mayores(tupla))

# EJERCICIO 7
print("------------------------------------")
"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def cuenta_empiezan_por(lista,car):
    # TODO: definir cuantos nombres quieres ingresar
    # TODO: definir una lista con el numero de elementos
    # TODO: pedir los nombres que pertenecen a la lista
    # TODO: definir por que letra comienza el nombre
    # TODO: imprimir la cantidad de nombres que empiezan por la letra
    
    cont=0
    for elemento in lista:
        if elemento.lower().startswith(car.lower()):
            cont+=1
    return cont
        
lista_nombres=["Ataulfo","Nicomedes","Javier","Julián","Aneto","Armando","Amando","Pepe","Zaratustra","Belén","Carmen","Julia"]
print(lista_nombres)
letra=input("Introduce letra de comienzo de los nombres: ")
print(f"Hay {cuenta_empiezan_por(lista_nombres,letra)} nombres de la lista que empiezan por {letra}")

# EJERCICIO 8
print("------------------------------------")
"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""
class Ejercicio8:
    def inicializar(self):
        self.cadena=input("Introduce palabra y te contaré las vocales: ").lower()
        
    def mostrar_resultados(conta,conte,conti,conto,contu):
        print(f"Tiene {conta} veces la letra a")
        print(f"Tiene {conte} veces la letra e")
        print(f"Tiene {conti} veces la letra i")
        print(f"Tiene {conto} veces la letra o")
        print(f"Tiene {contu} veces la letra u")
        
    def contar_vocales(self):
        # TODO: recibir una palabra
        # TODO: contabilizar cuantas letras tiene de "a"
        # TODO: contabilizar cuantas letras tiene de "e"
        # TODO: contabilizar cuantas letras tiene de "i"
        # TODO: contabilizar cuantas letras tiene de "o"
        # TODO: contabilizar cuantas letras tiene de "u"
        
        vocales=["a","á","e","é","i","í","o","ó","u","ú"]
        vocalesa=["a","á"]
        vocalese=["e","é"]
        vocalesi=["i","í"]
        vocaleso=["o","ó"]
        conta=0
        conte=0
        conti=0
        conto=0
        contu=0
        
        for letra in range(len(self.cadena)):
            if self.cadena[letra] in vocales:
                if self.cadena[letra] in vocalesa:
                    conta+=1
                elif self.cadena[letra] in vocalese:
                    conte+=1
                elif self.cadena[letra] in vocalesi:
                    conti+=1
                elif self.cadena[letra] in vocaleso:
                    conto+=1
                else: contu+=1
        
        return conta,conte,conti,conto,contu 

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
        
        # if opcion == 1:
        #     Ejercicio1.fun_ejercicio1()
        # elif opcion == 2:
        #     Ejercicio2.fun_ejercicio2()
        # elif opcion == 3:
        #     Ejercicio3.fun_ejercicio3()
        # elif opcion == 4:
        #     Ejercicio4.fun_ejercicio4()
        # elif opcion == 5:
        #     Ejercicio5.fun_ejercicio5()
        # elif opcion == 6:
        #     Ejercicio2.fun_ejercicio2()
        # elif opcion == 7:
        #     Ejercicio3.fun_ejercicio3()
        # el
        if opcion == 8:
            ejer8=Ejercicio8()
            ejer8.inicializar()
            resultado = ejer8.contar_vocales()
            print(resultado)
            print(resultado[0]) 
            print(resultado[1])
            print(resultado[2])
            print(resultado[3])
            print(resultado[4])
            ejer8.mostrar_resultados(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4])
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")