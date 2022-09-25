"""1)** Crea el siguiente programa:"
    "* Una clase de nombre Librería",
    "* Inicia los siguientes atributos: nombre, sección, editorial y año
    "* Crea una segunda clase con nombre Rosalia que herede la clase librería.
    "* En esta clase Rosalia, crea una función \"result\" cuyo resultado sea los datos de los libros.
    "* declara los Objetos siguientes:
    "    * libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
    "    * libro2 --> 33 Botones, Novela negra, Atlantis, 2022
    "    * libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022"
"""
class Libreria:
    def __init__(self,nombre, sección, editorial,año) -> None:
        self.nombre=nombre
        self.sección=sección
        self.editorial=editorial
        self.año=año
        
class Rosalia(Libreria):
    def result(self):
        print(self.nombre)
        print(self.sección)
        print(self.editorial)
        print(self.año)

"""
    "**2)** Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase, define una función de nombre misLibros, cuyo resultado sea los datos de los libros:
    "* libro4 --> Mi primera Novela, Novela, Bruño, 2019
    "* libro5 --> Gatos, Literatura, Listado, 2018"
    * Realiza la media de los años de los libros 4 y 5"
"""
class MiLibro(Libreria):
    def misLibros(self):
        print(f"La información del libro \"{self.nombre}\" es la siguiente: Sección \"{self.sección}\", Editorial \"{self.editorial}\" y Año {self.año}")

import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("**************** MENU *******************")
        print("************** EJERCICIOS ***************")
        print("***** 1. Los libros de Rosalía  *********")
        print("***** 2. Mis Libros *********************")
        print("***** 99. Salir (del menú) **************")
        print("*****************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:
            
            libro1=Rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
            libro1.result()
            libro2=Rosalia("33 Botones", "Novela negra", "Atlantis", 2022)
            libro2.result()
            libro3=Rosalia("Venganza en Compostela", "Historia", "Universo de letras", 2022)
            libro3.result()
                        
            click=input("Press to continue...")
        elif opcion == 2:

            libro4=MiLibro("Mi primera Novela", "Novela", "Bruño", 2019)
            libro4.misLibros()
            libro5=MiLibro("Gatos", "Literatura", "Listado", 2018)
            libro5.misLibros()  
            
            print("La media de los años es:",(libro4.año+libro5.año)/2)
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")