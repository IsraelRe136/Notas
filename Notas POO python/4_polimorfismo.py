class Gato():
    def sonido(self):
        return "mia"
    
class Perro():
    def sonido(self):
        return "clau"  
    
def hacer_sonido(animal):
    print(animal.sonido())


gato=Gato()
perro=Perro()

hacer_sonido(gato)