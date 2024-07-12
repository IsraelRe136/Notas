class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre=new_nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
dalto=Persona("lucas",21)

dalto.nombre="pepe"

del dalto.nombre

nombre=dalto.nombre

print(nombre)


