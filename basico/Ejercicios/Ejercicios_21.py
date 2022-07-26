# EJERCICIO 1

"""
    Escriba una función es_bisiesto() que determine si un año determinado es un año
    bisiesto. Un año bisiesto es divisible por 4, pero no por 100.
    También es divisible por 400.
"""
import os

class Ejercicio1:
  
  def es_bisiesto(anio):
        # TODO: bisiesto es divisible por 4
        # TODO: bisiesto NO es divisible por 100
        # TODO: bisiesto es divisible por 400
      
      if (anio%4==0) and ((anio%100!=0) or (anio%400==0)): return True
      else: return False

  def mostrar():
    for año in range(1982,2030):
      if Ejercicio1.es_bisiesto(año):print(f"El año {año} SI es bisiesto")
      else:print(f"El año {año} NO es bisiesto")
    
# EJERCICIO 2

"""
    Haz un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
    Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos
    esos años si cada año se aplica la tasa de interés introducida.
    Recordar que un capital C dolares a un interés del x por cien durante n años
    se convierte en C * (1 + x/100)elevado a n (años). Probar el programa
    sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""

class Ejercicio2:
  
  def __init__(self) -> None:
     self.capital=float(input("Introduzca Capital inicial: "))
     self.interes=float(input("Introduzca Interés a aplicar: "))
     self.años=int(input("Introduzca Número de años: "))
     
  def hipoteca(self):
    
      return (self.capital*pow((1 + self.interes/100),self.años))

  def hipoteca2(self):
    
      return self.capital*(1 + self.interes/100)**self.años
    
  def mostrar():
      ejer=Ejercicio2()
      print(round(ejer.hipoteca(),2))
      print(round(ejer.hipoteca2(),2))
    
# EJERCICIO 3

"""
    Este programa muestra primero el listado de categorías de películas
    y pide al usuario que introduzca el código de la categoría de la película
    y posterior a ello pide que el usuario introduzca el número de días de atraso,
    y así se muestra al final el total a pagar.
"""

# CATEGORIA     PRECIO  CODIGO  RECARGO/DIA DE ATRASO
# FAVORITOS      2.50      1          0.50
# NUEVOS         3.00      2          0.75
# ESTRENOS       3.50      3          1.00
# SUPER ESTRENOS 4.00      4          1.50
class VideoClubVHS:
  
  def __init__(self,categoria,precio,codigo,recargo_por_dia,espacio_mostrar) -> None:
     self.categoria=categoria
     self.precio=precio
     self.codigo=codigo
     self.recargo_por_dia=recargo_por_dia
     self.espacio_mostrar=espacio_mostrar
     
  def mostrar_catalogo(self):
     print(self.categoria+self.espacio_mostrar+str(self.precio)+"      "+str(self.codigo))
  
  def mostrar_deuda(self,dias):
    if dias!=0:
      deuda=self.precio+(self.recargo_por_dia*float(dias))
      print(f"Al usuario se le aplica un RECARGO/DIA DE ATRASO de {self.recargo_por_dia}, por lo que debe {deuda}")
    else: print(f"El usuario debe {self.precio}")

  def mostrar():
    categoria1=VideoClubVHS("FAVORITOS",2.50,1,0.50,"      ")
    categoria2=VideoClubVHS("NUEVOS",3.00,2,0.75,"         ")
    categoria3=VideoClubVHS("ESTRENOS",3.50,3,1.00,"       ")
    categoria4=VideoClubVHS("SUPER ESTRENOS",4.00,4,1.50," ")

    print("CATEGORIA     PRECIO  CÓDIGO  ")#RECARGO/DIA DE ATRASO")
    categoria1.mostrar_catalogo()
    categoria2.mostrar_catalogo()
    categoria3.mostrar_catalogo()
    categoria4.mostrar_catalogo()

    while True:
      opcion=int(input("Introduzca código de la categoría: "))
      dias_retraso=int(input("Introduzca días de retraso: "))

      if opcion==1:
        categoria1.mostrar_deuda(dias_retraso)
        break
      elif opcion==2:
        categoria2.mostrar_deuda(dias_retraso)
        break
      elif opcion==3:
        categoria3.mostrar_deuda(dias_retraso)
        break
      elif opcion==4:
        categoria4.mostrar_deuda(dias_retraso)
        break
      else: print("Introduce un código de categoría válido...1, 2, 3 ó 4 ")
	
# def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
#     os.system ("cls")

borrarPantalla=lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def funcion_menu():
    while True:
        
        print("\n")
        print("******************* MENU *******************")
        print("**************** EJERCICIOS ****************")
        print("***** 1. Detector de Años Bisiestos ********")
        print("***** 2. Calculadora de Capital ************")
        print("***** 3. Calculadora de Deuda VideoClub*****")
        print("***** 99. Salir (del menú) *****************")
        print("********************************************")
        print("\n")
        
        opcion = int(input("Inserte su opción: "))
        
        if opcion == 1:   
            borrarPantalla()
            Ejercicio1.mostrar()
        elif opcion == 2: 
            borrarPantalla()
            Ejercicio2.mostrar()
        elif opcion == 3: 
            borrarPantalla()
            VideoClubVHS.mostrar()
        elif opcion == 99:
            break
        else:
            print("por favor, escriba una opción correcta. ")
            print("\n")
            
funcion_menu()
print("Enhorabuena acabaste los ejercicios")