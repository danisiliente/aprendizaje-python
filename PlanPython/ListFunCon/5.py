#Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
#Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
#https://platzi.com/tutoriales/1937-python/1910-lista-de-ejercicios-en-python/

import random

def mayor(lista):
    mayor=0
    for i in range (len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def llenar(lis):
    cant = int(input('Tamaño de la lista: '))
    for i in range(cant):
        llenarLista = int(input('Ingrese números enteros: '))
        lis.append(llenarLista)
    return lis

def aleatoria(l):
    cant = int(input('Tamaño de la lista: '))
    for i in range(cant):
        l.append(random.randint(1,100))
    return l

lista = []

opcion = input('Desea llenar la lista manualmente o aleatoriamente: m/a ')

if opcion == 'm':
    print(llenar(lista))
elif opcion == 'a':
    print(aleatoria(lista))
else:
    print('No válido')
    exit()

print('El mayor es: ',mayor(lista))