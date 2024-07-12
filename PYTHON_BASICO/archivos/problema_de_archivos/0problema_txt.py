
nombres=["lucas","matias","fer","sopfia"]
apellidos=["dqalto","sin","cxarlols","domingues"]

with open("archivos\\problema_de _archivos\\nombres_y_apelñlidos.txt","w") as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"nombre {n} \n Apellido: {a} \n----------\n")for n,a in zip(nombres,apellidos)]