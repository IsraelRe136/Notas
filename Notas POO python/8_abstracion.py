class auto():
    def __init__(self):
        self.__estado="apagado"

    def encender(self):
        self._estado="encendido"
        print("el auto esta encendido")

    def conducir(self):
        if self._estado=="apagado":
            self.encender
        print("conmducir el auto ")

mi_autp=auto()

mi_autp.conducir()