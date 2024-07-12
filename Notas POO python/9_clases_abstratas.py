#no se pueden crear clases persona es como una plantilla
# que ahuevo tienes que definir esos atributos
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"hola mellamo {self.nombre}")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo):
        super().__init__(nombre,edad,sexo) 
    def hacer_actividad(self):
        print("estoy estudiando")

dalto=Estudiante("lucas",21,"maculino")

dalto.hacer_actividad()