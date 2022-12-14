#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)

import random

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente
print('lista: ',lista)

def menorMayor(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j],l[j + 1] = l[j + 1], l[j]
    print("- a +  ",l)

def mayorMenor(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] < l[j + 1]:
                l[j],l[j + 1] = l[j + 1], l[j]
    print("+ a -  ",l)

menorMayor(lista)
mayorMenor(lista)