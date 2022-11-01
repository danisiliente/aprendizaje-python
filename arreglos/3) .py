#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Sume los pares y saque el promedio de los impares

import random

tamaño = random.randint(10,25)

lista = []

for i in range(tamaño):
    lista.insert(i,round(random.random()*100))
print("Lista: ",lista)

sumapar = 0
pares = []
impares = []
sumaimpar = 0

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
        sumapar += lista[i] 
    else:
        impares.append(lista[i])
        sumaimpar += lista[i]
print("Pares: ",pares,"\nSuma de los pares = ",sumapar)
print("Impares: ",impares,"\nPromedio de los impares = ",sumaimpar // len(impares))