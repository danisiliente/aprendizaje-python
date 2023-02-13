#Escribir una función sum() y una función multip() que sumen y multipliquen
#respectivamente todos los números de una lista. Por ejemplo:
#sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
#https://platzi.com/tutoriales/1937-python/1910-lista-de-ejercicios-en-python/

def suma(lis):
    sum = 0
    for e in lis:
        sum += e
    return sum

def multi(lis):
    mul = 1
    for i in lis:
        mul *= i
    return mul

def llenar(lis):
    cant = int(input('Tamaño de la lista: '))
    for i in range(cant):
        llenarLista = int(input('Ingrese números enteros: '))
        lis.append(llenarLista)
    return lis

lista = []

print(llenar(lista))
print(suma(lista))
print(multi(lista))
