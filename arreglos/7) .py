#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Encuentre la suma y el promedio de los números de la lista

import random

tamaño = random.randint(10,25)

lista = []

for i in range(tamaño):
    lista.insert(i,round(random.random()*100))
print(lista," Tamaño: ",i + 1)

suma = 0
promedio = 0

for i in range(len(lista)):
    suma += lista[i]
    promedio = suma // len(lista)
print("La suma es: ",suma,"\nEl promedio es: ",promedio)