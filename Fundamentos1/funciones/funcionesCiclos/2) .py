#Solicitar al usuario un número de hasta 9 dígitos e 
#imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576 

def invertir(n):
    inverso = 0
    while n > 0:
        residuo = n % 10
        inverso = (inverso * 10) + residuo
        n //= 10
    return inverso

numero = int(input("Ingrese un número: "))
print(invertir(numero))