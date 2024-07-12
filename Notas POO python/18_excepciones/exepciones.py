def sumar ():
    while True: 
        a = input(" number")
        b = input(" number")
        try:
                resultado= int(a)+int(b)
        except Exception: 
            print("xd")
        else:
            break
        finally:
            print("eso se ejecuta siempre")

    return resultado

print(sumar())

