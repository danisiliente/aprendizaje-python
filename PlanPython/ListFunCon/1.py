# Haz un programa que, dada una lista a cualquiera, sustituya
# cualquier elemento negativo por 0. - pag 190

def llenar(lis):
    llenarLista = int(input('Ingrese números enteros: '))
    lis.append(llenarLista)

lista = []

long = int(input('Tamaño de la lista: '))

while len(lista) < long:
    llenar(lista)

def solucion(l):
    for i in range(len(l)):
        if l[i] < 0:
            l[i] = 0
    return l

print(lista)
print(solucion(lista))