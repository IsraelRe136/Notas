
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,new_nombre):
        self.__nombre=new_nombre


dalto=Persona("lucas",21)

nombre=dalto.get_nombre()
print(nombre)
dalto.set_nombre("pepito")

nombre=dalto.get_nombre()
print(nombre)






