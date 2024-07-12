# with open("archivos\\texto.txt",'w') as archivo: #a  agrega no sobreescribe
#     # archivo.write("holiiii")
#     archivo.writelines([" como andass capo \n","misericordia"])
    

with open("archivos\\texto.txt",'a') as archivo: #a  agrega no sobreescribe
    # archivo.write("holiiii")
    for i in range (5) :
        archivo.write(f"liena {i+1} agregada \n")
