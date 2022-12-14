#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista.

import random


lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente - Comprensión
print(lista,' tamaño:', len(lista))

def sumProm(l):
    suma = 0
    promedio = 0

    for i in range(len(l)):
        suma += l[i]
        promedio = suma // len(l)
    print("La suma es: ",suma,"\nEl promedio es: ",promedio)

    for i in range(len(l)):
        if l[i] < promedio:
            print("El número",l[i],"está por debajo del promedio -->",promedio)
        elif l[i] > promedio:
            print("El número",l[i],"está por encima del promedio -->",promedio)
        else:
            print("El número",l[i],"es igual al promedio -->",promedio)

sumProm(lista)