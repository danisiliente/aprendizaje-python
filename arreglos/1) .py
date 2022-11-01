#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista.

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

for i in range(len(lista)):
    if lista[i] < promedio:
        print("El número",lista[i],"está por debajo del promedio -->",promedio)
    elif lista[i] > promedio:
        print("El número",lista[i],"está por encima del promedio -->",promedio)
    else:
        print("El número",lista[i],"es igual al promedio -->",promedio)