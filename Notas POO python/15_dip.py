# class Diccionario:
#     def verificar_palabra(self,palabra):
#         pass

# class correctorOrtografico:
#     def __init__(self):
#         self.diccionario=Diccionario()

#     def corregir_texto(self,texto):
#         pass

from abc import ABC, abstractmethod

class verificasddorortografico():
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(verificasddorortografico):
    def verificar_palabra(self, palabra):
        pass
class SercicioOnliine(verificasddorortografico):
    def verificar_palabra(self, palabra):
        pass


class CoreectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):


corrector = CoreectorOrtografico(Diccionario())