#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Muestre cuales y cuantos son primos

import random

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente
print(lista,' tamaño:', len(lista))

def primos(l):
    for i in range(len(lista)):
        divisores = 0
        for j in range(1,101):
            if lista[i] % j == 0:
                divisores += 1
        if divisores == 2:
            l.append(lista[i])
    print("Hay",len(l),"números primos","\nSon los siguientes: ",l)

listaPrimos = []

primos(listaPrimos)