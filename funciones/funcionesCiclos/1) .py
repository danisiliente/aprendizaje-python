#Calcular la operación x^n sin utilizar la función pow

def calcPotencia(n,p):
    elevado = n
    while p > 1:
        elevado *= n
        p -= 1
    return elevado

numero = int(input('Ingrese un número: '))
potencia = int(input('Ingrese la potencia: '))

print(calcPotencia(numero,potencia))