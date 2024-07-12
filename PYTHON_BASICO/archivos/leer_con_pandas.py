import pandas as pd

df=pd.read_csv("archivos\\csv.csv")
df2=pd.read_csv("archivos\\csv.csv")
# print(df["name"])

df_ordenado=df.sort_values("edad")

df_ordenado=df.sort_values("edad",ascending=False)

df_concatenado=pd.concat([df,df2])

primer_fila=df.head(1) #tail para las ultimas

filas_y_columnas=df.shape

df_info=df.describe()

elemto_especifico=df.loc[2,"edad"] #iloc [2,4]

apelllidos=df.iloc[:,1]

print(apelllidos)

# cadena="0123456789"

# print(cadena[0:6])

