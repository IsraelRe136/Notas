def decorador(funcion):
    def funcion_modificada():
        print("antes de llamar a las funcion ")
        funcion()
        print("despues de llmar a la funcion ")
    return funcion_modificada


# def saludo():
#     print("hola dalto")

# saludo_modificado=decorador(saludo)

# saludo_modificado()

@decorador
def saludo():
    print("hola dalto")
    

saludo()
