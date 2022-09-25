"""
    "**1)** Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
    "
    "* Un constructor, donde los datos pueden estar vacíos.
    "* mostrar(): Muestra los datos de la persona.
    "* esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad."
"""
def resultadoMayoriaEdad(persona):
    if persona.esMayorDeEdad():
        print("Es MAYOR de Edad")
    else: print("Es MENOR de Edad")
class Persona:
    def __init__(self,nombre, edad, DNI) -> None:
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    # def __init__(self) -> None:
    #     self.nombre=""
    #     self.edad=0
    #     self.DNI=""    
    def mostrar(self) -> None:
        print(f"La información de la Persona es: Nombre - \"{self.nombre}\", Edad - {self.edad}, DNI - \"{self.DNI}\"")
        
    def esMayorDeEdad(self):
        if self.edad<18:
            return False
        else: return True
"""
    "**2)** Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
    "
    "* Un constructor, donde los datos pueden estar vacíos.
    "* El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    "* mostrar(): Muestra los datos de la cuenta.
    "* ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    "* retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo."

    "* Ingresar en positivo"

    "* Ingresar en negativo"

    "* Retirar dinero"

    "* Retirar dinero en numeros rojos"
"""
class Cuenta(Persona):
    
    def __init__(self,nombre, edad, DNI,titular, cantidad=0) -> None:
        super().__init__(nombre, edad, DNI)
        self.titular=titular
        self.cantidad=0
    # def __init__(self,titular, cantidad) -> None:
    #     self.titular=titular
    #     self.cantidad=cantidad 
    def mostrar(self) -> None:
        print(f"La información del Titular Cuenta es: Nombre - \"{self.nombre}\", Edad - {self.edad}, DNI - \"{self.DNI}\"")
        print(f"La información de la Cuenta es: Titular - \"{self.titular}\", Cantidad en la cuenta: {self.cantidad}")
        
    def ingresar(self, ingreso) -> None:
        if ingreso<=0:
            pass
        else: self.cantidad+=ingreso
        
    def retirar(self, retirada) -> None:
        if self.cantidad<=0:
            print("¡OJO! - Va a realizar retirada de efectivo, pero su cuenta está en número rojos")
        self.cantidad-=retirada
        if self.cantidad<=0:
            print("¡OJO! - La cuenta está en número rojos")
"""
    "**3)** Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular 
    y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:
    "
    "* Un constructor.
    "* En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., 
    por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    "* Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    "* El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    "* Piensa los métodos heredados de la clase madre que hay que reescribir."

    "* Mayor de edad"

    "* Menor de edad"
"""
class CuentaJoven(Cuenta):
    
    def __init__(self,nombre, edad, DNI,titular,bonificación) -> None:
        super().__init__(nombre, edad, DNI,titular)
        self.bonificación=bonificación
    # def __init__(self,titular, cantidad) -> None:
    #     self.titular=titular
    #     self.cantidad=cantidad 
    def mostrar(self) -> None:
        print("¡Cuenta Joven!")
        print(f"La información del Titular Cuenta es: Nombre - \"{self.nombre}\", Edad - {self.edad}, DNI - \"{self.DNI}\"")
        print(f"La información de la Cuenta es: Titular - \"{self.titular}\", Cantidad en la cuenta: {self.cantidad} y la Bonificación es del {self.bonificación}%")
        
    def esTitularValido(self):
        if self.edad<25 and self.esMayorDeEdad():
            return True
        else: return False
        
    def retirar(self, retirada) -> None:
        
        if self.esTitularValido():
                super().retirar(retirada)
        else: print("Titular no válido, sólo menores de 25 y mayores de 18!")
import os

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def funcion_menu():
    while True:
        #C:\Users\Matusaleno\Documents\Apuntes\Curso Data Science\Ejercicios\Míos\Dataset\git_test\Data-Science\media
        borrarPantalla()
        print("**************** MENU *******************")
        print("************** EJERCICIOS ***************")
        print("***** 1. Personas ***********************")
        print("***** 2. La Cuenta Bancaria *************")
        print("***** 3. La Cuenta Joven ****************")
        print("***** 99. Salir (del menú) **************")
        print("*****************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:
            #persona1=Persona()
            persona2=Persona("Javier",40,"55555555L")      
            persona3=Persona("Carmen",3,"11111111L")
            persona4=Persona("Julia",0.9,"22222222Ñ")
            persona5=Persona("Lucía",40,"666666666Ñ")
            
            persona2.mostrar()
            resultadoMayoriaEdad(persona2)
            
            persona3.mostrar()
            resultadoMayoriaEdad(persona3)
            
            persona4.mostrar()
            resultadoMayoriaEdad(persona4)
            
            persona5.mostrar()
            resultadoMayoriaEdad(persona5)
                                    
            click=input("Press to continue...")
        elif opcion == 2:
            
            cuentajavi=Cuenta("Javier",40,"55555555L","Javi")
            cuentajavi.cantidad=2000
            cuentajavi.mostrar()     
            
            print("Ingreso 200")
            cuentajavi.ingresar(200)
            cuentajavi.mostrar()  
               
            click=input("Press to continue...")
                       
            print("Retiro 200")
            cuentajavi.retirar(200)
            cuentajavi.mostrar()  
               
            click=input("Press to continue...")
                       
            print("Retiro 1200")
            cuentajavi.retirar(1200)
            cuentajavi.mostrar()  
               
            click=input("Press to continue...")
                       
            print("Retiro 1200")
            cuentajavi.retirar(1200)
            cuentajavi.mostrar()  
               
            click=input("Press to continue...")
               
        elif opcion == 3:
            
            cuentajovenjavi=CuentaJoven("Javier",40,"555555555J","Javi",15)
            cuentajovencarmen=CuentaJoven("Carmen",3,"2222222222H","Karme",30)
            cuentajovenjulia=CuentaJoven("Julia",19,"444444444444l","jupli",45)
            
            
            cuentajovenjavi.mostrar()
            print("Ingreso 1200")
            cuentajovenjavi.ingresar(1200)            
            cuentajovenjavi.mostrar()
                           
            click=input("Press to continue...")
            
            print("Retiro 200")
            cuentajovenjavi.retirar(200)            
            cuentajovenjavi.mostrar()
                      
            click=input("Press to continue...")               
            
            cuentajovencarmen.mostrar()
            print("Ingreso 1200")
            cuentajovencarmen.ingresar(1200)            
            cuentajovencarmen.mostrar()
                           
            click=input("Press to continue...")
            
            print("Retiro 200")
            cuentajovencarmen.retirar(200)            
            cuentajovencarmen.mostrar()
                                                
            click=input("Press to continue...")
            
            cuentajovenjulia.mostrar()            
            print("Ingreso 1200")
            cuentajovenjulia.ingresar(1200)            
            cuentajovenjulia.mostrar()
                           
            click=input("Press to continue...")
            
            print("Retiro 200")
            cuentajovenjulia.retirar(200)            
            cuentajovenjulia.mostrar()
                                       
            click=input("Press to continue...")
            
            print("Retiro 1000")
            cuentajovenjulia.retirar(1000)            
            cuentajovenjulia.mostrar()
            
            click=input("Press to continue...")
            
            print("Retiro 20")
            cuentajovenjulia.retirar(20)            
            cuentajovenjulia.mostrar()
            
            click=input("Press to continue...")
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")