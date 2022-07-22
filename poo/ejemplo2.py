#Método 2
class Cliente:
    def inicializar(self,nombre) -> None:
        self.nombre=nombre
        
    def imprimir(self):
        print("Nombre", self.nombre)
        
cliente1=Cliente()
cliente1.inicializar("María")
cliente1.imprimir()

cliente2=Cliente()
cliente2.inicializar("Luis")
cliente2.imprimir()