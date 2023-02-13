#Calcular la operación x^n sin utilizar la función pow

numero = int(input("Digite el número: "))
potencia = int(input("Digite el exponente: "))

potenciaInicial = potencia
elevado = numero #Valor inicial del número a ser elevado

while potencia > 1:
    elevado *= numero
    potencia -= 1 #Cuando la potencia queda en 1, sale del bucle

print("El número",numero,"Elevado a la",potenciaInicial, "es: ",elevado)