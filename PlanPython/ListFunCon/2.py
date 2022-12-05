#Diseña un programa que lea una lista de 1O enteros, pero asegurándose de que todos
#los números introducidos por el usuario son positivos Cuando un número sea negativo,
#lo indicaremos con un mensaje y permitiremos al usuario repetir el intento cuantas veces sea preciso. - pag 197

def llenar(lis):
    llenarLista = int(input('Ingrese números enteros: '))
    if llenarLista < 0:
        llenarLista = int(input('--> Solo números POSITIVOS: '))
    else:
        lis.append(llenarLista)

lista = []

while len(lista) < 10:
    llenar(lista)

print(lista)
