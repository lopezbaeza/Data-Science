#Método 1
class Empleado:
    def __init__(self,Id,Name,Age,Role) -> None:
        self.Id=Id
        self.Name=Name
        self.Age=Age
        self.Role=Role
        
empleado1=Empleado(1,"Ana",30,"ingeniero")
empleado2=Empleado(2,"Pedro",45,"arquitecto")
empleado3=Empleado(3,"Andrea",25,"abogada")

print(empleado1.Age)
print(empleado3.Name)