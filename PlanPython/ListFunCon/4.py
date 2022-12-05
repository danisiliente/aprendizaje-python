#Diseña una función que reciba una lista de números y devuelva otra lista
#en la que cada elemento sea el doble del que tiene el mismo indice en la lista original.
#La lista original no debe sufrir ninguna modificación tras la llamada a la misma. - pag 275

lista = []
elDoble = []

def llenarLista(l):
    num = int(input('Ingrese números enteros: '))
    l.append(num)
    print(l)

def doble(lis1,lis2):
    for i in lis1:
        lis2.append(i * 2)
    print(lis2)

tam = int(input('Tamaño de la lista: '))

while len(lista) < tam:
    llenarLista(lista)

doble(lista,elDoble)