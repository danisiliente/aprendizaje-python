#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Encuentre la suma y el promedio de los números de la lista

import random

def ramdonlist(lis):
    lis = [round(random.random()*100) for i in range(random.randint(10,25))] #Comprensión
    print(lis,' tamaño:', len(lis))
    return lis

def sumprom(lis):
    suma = 0
    promedio = 0
    for i in range(len(lis)):
        suma += lis[i]
        promedio = suma // len(lis)
    print("La suma es: ",suma,"\nEl promedio es: ",promedio)

lista = []
listafinal = (ramdonlist(lista))
sumprom(listafinal)