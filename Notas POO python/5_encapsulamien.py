class MiClase:
    def __init__(self):
        self.__atributo_privado="valor"

    def __hablar(self):
        print("hola ")
objet=MiClase(  )
print(objet.__atributo_privado)