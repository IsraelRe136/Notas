import pandas as pd

df=pd.read_csv("archivos\\problema_de_archivos\\csv.csv")
df['edad']=df['edad'].astype(str)
print(type((df['edad'][0])))