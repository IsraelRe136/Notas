class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"cometiste el siguiente error {err}")

try:
    raise MiExcepcion("hjahaha")
except:
    print("como cometiste ese error")