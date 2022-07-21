#2)Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

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

x=pide_input("Introduce número...")
y=pide_input("Introduce número...")
z=pide_input("Introduce número...")

print(f"El número mayor es {max_de_tres(x,y,z)}")

print(f"El número mayor con fun2 es {max_de_tres_v2(x,y,z)}")