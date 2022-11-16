#llenar una tupla de tamaño 10 a 25, llenarla con números aleatorios entre 0 y 100 y decir cuáles son primos.

import random

tupla = tuple(round(random.random()*100) for i in range(random.randint(10,25)))

print(tupla)

primos = []

'''for i in range(len(tupla)):
    divisores = 0
    for j in range(1,101):
        if tupla[i] % j == 0:
            divisores += 1
    if divisores == 2:
        primos.append(tupla[i])
        
print("Hay",len(primos),"números primos","\nSon los siguientes: ",primos)'''

for i in tupla:
    cont = 0
    for j in range(1,i):
        if i % j == 0:
            cont += 1
    if cont == 1:
        print('primo',i)