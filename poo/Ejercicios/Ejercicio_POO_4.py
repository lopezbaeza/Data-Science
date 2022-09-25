# EJERCICIO 1

"""
    Crea una clase persona. Sus atributos deben ser su nombre y su edad.
    Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
"""

class Persona_0_1:

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self) -> None:
        self.edad +=  1

# EJERCICIO 2

"""
    Para la clase anterior definir el método str.
    Debe retornar al menos el nombre de la persona.
"""

def imprimir(algo):
    print(algo)
    
class Persona_0_2:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
        
    def __str__(self):
        return self.nombre + " tiene " + str(self.edad) + " años"
        
    def cumpleaños(self) -> None:
        self.edad +=  1

# EJERCICIO 3

"""
    Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto).
    El saldo representa el dinero que tiene la persona.
    El método transferencia hace que la Persona que llama el método le transfiera la cantidad monto al objeto persona2.
    Si no tiene el dinero suficiente no se ejecuta la acción.
"""

class Persona_0_3:
    def __init__(self,nombre,edad,saldo):
        self.nombre=nombre
        self.edad=edad
        self.saldo=saldo
        
    def __str__(self):
        return self.nombre + " tiene " + str(self.edad) + " años y un saldo de "+ str(self.saldo)
        
    def cumpleaños(self):
        self.edad=self.edad+1
        
    def transferencia(self, persona2, monto):
        if monto>self.saldo:
            print("El saldo de la cuenta es insuficiente")
        else:
            persona2.saldo=persona2.saldo+monto
            self.saldo=self.saldo-monto

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
        print("***** 99. Salir (del menú) **************")
        print("*****************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:
        
            javi=Persona_0_1("Javi",39)
            print(javi.nombre + " Tiene " + str(javi.edad))
            javi.cumpleaños()
            print(javi.nombre + " Tiene " + str(javi.edad))
                                    
            click=input("Press to continue...")
        elif opcion == 2:
                   
            matu = Persona_0_2("Javier",39)

            imprimir(matu)
            matu.cumpleaños()

            imprimir(matu)               
                                    
            click=input("Press to continue...")
        elif opcion == 3:
            
            p1=Persona_0_3("Javier",39,1000)
            p2=Persona_0_3("Ahmed",30,300)
            
            print(p1)
            print(p2)
                                    
            click=input("Press to continue...")
            
            print("Transferencia de 300")
            p1.transferencia(p2,300)
            print(p1)
            print(p2)
                                    
            click=input("Press to continue...")            
            
            print("Transferencia de 700")
            p1.transferencia(p2,700)
            print(p1)
            print(p2)            
                                    
            click=input("Press to continue...")            
            
            print("Transferencia de 300")
            p1.transferencia(p2,300)
            print(p1)
            print(p2)
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")