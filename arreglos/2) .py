#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Muestre cuales y cuantos son primos

import random

'''tamaño = random.randint(10,25)

lista = []

for i in range(tamaño):
    lista.insert(i,round(random.random()*100))
print(lista," Tamaño: ",i + 1)'''

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente
print(lista,' tamaño:', len(lista))

primos = []

for i in range(len(lista)):
    divisores = 0
    for j in range(1,101):
        if lista[i] % j == 0:
            divisores += 1
    if divisores == 2:
        primos.append(lista[i])
print("Hay",len(primos),"números primos","\nSon los siguientes: ",primos)