import csv
from claseBase import *

datos = []

with open('database.csv') as file:
    
    file = csv.reader(file)
    
    for datos in file:
        empresa = Empresa(datos[1], datos[2], datos[4], datos[6])
        datos.append(empresa)
        
print(datos)

for d in datos:
    print(d.nombreCompleto())