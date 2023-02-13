#Diseña una función que, dada una lista de números, devuelva otra lista 
#que solo incluga sus números impares. - pag 262

lista = []

def llenarLista(l):
    num = int(input('Ingrese números enteros: '))
    l.append(num)
    return l

tam = int(input('Tamaño de la lista: '))

while len(lista) < tam:
    llenarLista(lista)

impares = []

for n in lista:
    if n % 2 != 0:
        impares.append(n)

print('Lista original: ',lista,'\nLista con impares: ',impares)