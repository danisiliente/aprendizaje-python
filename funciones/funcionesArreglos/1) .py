#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que 
#posiciones esta. Si no está agréguelo al final de la lista.

import random

def ramdonlist(lis):
    lis = [round(random.random()*100) for i in range(random.randint(10,25))] #Comprensión
    print(lis,' tamaño:', len(lis))

lista = []
ramdonlist(lista)
