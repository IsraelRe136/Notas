# class Celular():
#     propiedad="valor1"
#     modelo="s23"

# celular1= Celular()

# print(celular1.modelo)

class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca= marca
        self.modelo=modelo
        self.camara=camara
    
    def llamar(self):
        print(f'estas llamando desde {self.modelo}')



celular1= Celular("samnsung","s23","48mpx")
celular2= Celular("samnsung","s24","98mpx")

celular2.llamar()

class Estudiante:
    def __init__(self,nombre,edad,grado) 
        self.nombre=nombre
        self.edad=edad
        self.grado=grado

    def estudiar(self);

nombre=input("")
edad=input("")
grado=input("")

estudiante=Estudiante(nombre,edad,grado)


while True:
    estudiar=input()
    if(estudiar.lower()== "estudiar"):
        estudiante.estudiar

