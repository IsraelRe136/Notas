class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return f'Persona(nombre={self.nombre})'
    def __repr__(self):
        return f'{self.nombre}'
    def __add__(self,otro):
        nuevo_valor=self.edad+otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

dalto=Persona("luvcas",21)
pedro=Persona("lucas",21)
maria=Persona("maria",45)
resul=dalto+pedro+maria
print(resul.edad)