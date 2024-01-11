#generar lista con sublistas aleatorias de 2 a 5

import random

'''lista = [[] for filas in range(random.randint(2,5))]

print(lista)

columnas = round(random.randint(2,5))

for i in lista:
    for j in range(columnas):
        i.append(round(random.random()*100))
print(lista)'''

columnas = round(random.randint(2,5))
lista = [[round(random.random()*100) for col in range(columnas)] for fil in range(random.randint(2,5))]

print(lista)

        