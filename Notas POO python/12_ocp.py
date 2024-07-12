class notificador:
    def __init__(self,usuario,mensaje):
        self.usuario=usuario
        self.mensaje=mensaje
    
    def notificar(self):
        raise NotImplementedError


class notificador_emai(notificador):
    def notificar(self):
        print(f"enviameos mensaje mail a {self.usuario.email}")