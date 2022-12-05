# Haz un programa que, dada una lista a cualquiera, sustituya
# cualquier elemento negativo por 0. - pag 190

def llenar(lis):
    llenarLista = int(input('Ingrese números enteros: '))
    lis.append(llenarLista)

lista = []

long = int(input('Tamaño de la lista: '))

while len(lista) < long:
    llenar(lista)

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0

print(lista)