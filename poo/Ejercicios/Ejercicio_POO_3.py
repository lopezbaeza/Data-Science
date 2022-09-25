
# EJERCICIO 1

"""
    Crearemos una clase llamada NumeroComplejo.
    Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y.
    Representa un número complejo de la forma (x, y).
"""

class NumeroComplejo_0_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# EJERCICIO 2

"""
    Ahora defina dentro de la clase NumeroComplejo un función imprimir
    donde muestre los valores de x e y.
"""


class NumeroComplejo_0_2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def imprimir(self):
        print(f"Coordenada X: {self.x} - Coordenada Y: {self.y}")

# EJERCICIO 3

"""
    Define la función str para la clase NumeroComplejo
    para poder imprimir usando la función print.
"""

class NumeroComplejo_0_3:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "Coordenada X: " + str(self.x)+ " - Coordenada Y: "+ str(self.y)
    def imprimir(self):
        print(f"Coordenada X: {self.x} - Coordenada Y: {self.y}")

# EJERCICIO 4

"""
    Define una función que compara dos números complejos,
    ya que si dos objetos distintos tienen sus atributos iguales,y
    sino NO se consideran iguales.
"""


class NumeroComplejo_0_4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"Coordenada X: {self.x} - Coordenada Y: {self.y}"

    def __str__(self):
        return "Coordenada X: " + str(self.x)+ " - Coordenada Y: "+ str(self.y)

    def son_iguales(self, numc2):
        if self.x == numc2.x and self.y == numc2.y:
            return True
        return False

# EJERCICIO 5

"""
    Realiza un método que sume dos numeros complejos sin modificiar los objetos originales,
    ya que se retorna un nuevo numero NumeroComplejo.
"""

class NumeroComplejo_0_5:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"Coordenada X: {self.x} - Coordenada Y: {self.y}"

    def __str__(self):
        return "Coordenada X: " + str(self.x)+ " - Coordenada Y: "+ str(self.y)

    def son_iguales(self, numc2):
        if self.x == numc2.x and self.y == numc2.y:
            return True
        return False

    def sumacomplejos(self,numc2):
        return NumeroComplejo_0_5(self.x+numc2.x,self.y+numc2.y)

import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("**************** MENU *******************")
        print("************** EJERCICIOS ***************")
        print("***** 1. Ejercicio 1 ********************")
        print("***** 2. Ejercicio 2 ********************")
        print("***** 3. Ejercicio 3 ********************")
        print("***** 4. Ejercicio 4 ********************")
        print("***** 5. Ejercicio 5 ********************")
        print("***** 99. Salir (del menú) **************")
        print("*****************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:
        
            nc1 = NumeroComplejo_0_1(1, 2)

            print(f"Coordenada X: {nc1.x} - Coordenada Y: {nc1.y}")
                                    
            click=input("Press to continue...")
        elif opcion == 2:
                   
            nc2 = NumeroComplejo_0_2(3, 4)
            nc2.imprimir()
               
            click=input("Press to continue...")
               
        elif opcion == 3:
            
            nc3=NumeroComplejo_0_3(5,7)
            
            print(f"Pruebo str1 {nc3}")
            print("Pruebo str2 ",nc3)
            print(nc3)
            nc3.imprimir()
            
            click=input("Press to continue...")
        
        elif opcion == 4:
                   

            nc4_1 = NumeroComplejo_0_4(1, 2)
            nc4_2 = NumeroComplejo_0_4(1, 6)

            nc4_1.imprimir()
            print(f"{nc4_2}")
            
            print("Son Iguales?",nc4_1.son_iguales(nc4_2))
               
            click=input("Press to continue...")
               
            nc4_3 = NumeroComplejo_0_4(1, 6)

            nc4_3.imprimir()
            print(f"{nc4_2}")
            
            print("Son Iguales?",nc4_3.son_iguales(nc4_2))
               
            click=input("Press to continue...")
        elif opcion == 5:     
            
            nc5_1=NumeroComplejo_0_5(7,8)
            nc5_2=NumeroComplejo_0_5(4,7)
            
            print(f"Sumamos:{nc5_1} con {nc5_2}")
            ncsuma=nc5_1.sumacomplejos(nc5_2)

            print("Resultado:")
            ncsuma.imprimir()
            print(f"Resultado: {ncsuma}")


            nc5_3=NumeroComplejo_0_5(7,9)
            
            print(f"Sumamos:{nc5_3} con {nc5_2}")
            ncsuma2=nc5_2.sumacomplejos(nc5_3)

            print("Resultado:")
            ncsuma2.imprimir()
            print(f"Resultado: {ncsuma2}")
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")