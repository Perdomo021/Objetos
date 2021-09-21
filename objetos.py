print("Hola mundo OOP POO")

def transportarf(per):
    print("Estoy transportando",per,"personas")
    
class carro():
    
    def __init__(self, name):
        self.nombre = name
        
    def acelerar(self):
        print("Estoy acelerando")
        
    def transportar(self,per):
        print("Estoy transportando",per,"personas",self.nombre)
        
bmw01 = carro("bmw01") #crea el objeto
bmw01.acelerar()
bmw01.transportar(4)

mazda01 = carro("mazda01") #crea el objeto
mazda01.transportar(8)

bmw01.transportar(10)
transportarf(20)