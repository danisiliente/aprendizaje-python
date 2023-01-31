# Módulo de prueba para Listas

import random

def listaAleatoria(l):
    tamaño = int(input('Tamaño de la lista: '))
    for i in range(tamaño):
        l.append(random.randint(1,100))
    return l

def paresEnLista(l):
    pares = []
    for i in l:
        if i % 2 == 0:
            pares.append(i)
    return pares

def imparesEnLista(l):
    impares = []
    for i in l:
        if i % 2 != 0:
            impares.append(i)
    return impares

def sumarTodoLista(l):
    suma=0
    for elemento in l:
        suma += elemento
    return suma

def elevarTodoLista(l):
    cuadrados = []
    for elemento in l:
        cuadrados.append(elemento**2)
    return cuadrados