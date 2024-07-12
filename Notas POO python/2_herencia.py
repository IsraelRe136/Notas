
class Persona:
    def __init__(self,nombre,edad,nacionalidad) :
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def hablar(self):
        print("hablando")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        print(f"mi habilidsad es {self.habilidad}")


# herencia multiple
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad,nacionalidad, habiliadad,salario , empresa):
        Persona.__init__(self,nombre,edad,nacionalidad,)
        Artista.__init__(self,habiliadad)
        self.salario=salario
        self.empresa=empresa
    def mostrar_habilidad(self):
        print("no tengo ")

    def presentarse(self):
        return(f'{super().mostrar_habilidad()}')


roberto=EmpleadoArtista("roberto",14,"argentino","programado",45,"kuma")


herencia=issubclass(EmpleadoArtista,Persona)

instancia=isinstance(roberto,Artista)

print(instancia)