#1)Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
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

x=pide_input("Introduce número...")
y=pide_input("Introduce número...")

print(f"El número mayor es {max(x,y)}")