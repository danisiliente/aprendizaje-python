#Definir una función superposicion() que tome dos listas y devuelva True 
#si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
#Escribir la función usando el bucle for anidado.
#https://platzi.com/tutoriales/1937-python/1910-lista-de-ejercicios-en-python/

import random

def superposicion(l1,l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False

def aleatoria(l):
    cant = int(input('Tamaño de la lista: '))
    for i in range(cant):
        l.append(random.randint(1,10))
    return l

lista1 = []
lista2 = []

print(aleatoria(lista1))
print(aleatoria(lista2))
print(superposicion(lista1,lista2))