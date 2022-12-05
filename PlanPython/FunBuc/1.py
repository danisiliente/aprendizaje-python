#Diseña una función sin argumentos que devuelva un número aleatorio 
#mayor o igual que 0 y menor que 10. Puedes llamar a la función random desde tu función. - pag 246

import random

def alea():
    n = random.randint(0,10)
    print(n)

l = int(input('Cuántos números quiere imprimir: '))

for i in range(l):
    alea()

#Diseña una función sin argumentos que devuelva un número aleatorio 
#mayor o igual que -10 y menor que 10. - pag 246

def alea():
    n = random.randint(-10,10)
    print(n)

l = int(input('Cuántos números quiere imprimir: '))

for i in range(l):
    alea()
