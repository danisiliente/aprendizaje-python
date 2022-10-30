#Generar numero (generarlo random) y adivinarlo diciendo si cada intento es mayor o menor que el numero. 
#Decir cuantos numeros ingreso antes de adivinarlo

import random

print('Adivina el número')

adivinar = random.randint(1,100)

intentos = 0

numero = int(input("Ingrese un número: "))

while numero != adivinar:
    intentos += 1
    if numero < adivinar:
        print("Estás por debajo del número.")
    else:
        print("Estás por encima del número.")
    print("intentos = ",intentos)
    numero = int(input("Ingrese un número: "))

else:
    print("Adivinaste. El número era: ",adivinar)
    
