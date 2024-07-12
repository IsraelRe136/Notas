import csv

with open("archivos\\csv.csv") as archivo:
    reader=csv.reader(archivo)
    for row in reader:
        print(row)