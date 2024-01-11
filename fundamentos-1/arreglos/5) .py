#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que 
#posiciones esta. Si no está agréguelo al final de la lista.

import random

'''tamaño = random.randint(10,25)

lista = []

for i in range(tamaño):
    lista.insert(i,round(random.random()*100))
print("Lista: ",lista)'''

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente
print('Lista:',lista)

numero = int(input("Ingrese un número para buscar en la lista: "))

veces = 0
posiciones = []

for i in range(len(lista)):
    if numero == lista[i]:
        veces += 1
        posiciones.append(i)
if veces > 0:
    print("El número ingresado está",veces,"veces.","\nLas posiciones del número son: ",posiciones)
else:
    print("El número no está en la lista, así que fue agregado.")
    lista.append(numero)
    print("Lista: ",lista)