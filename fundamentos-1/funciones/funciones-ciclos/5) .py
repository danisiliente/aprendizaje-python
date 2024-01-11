#Determinar si un numero es o no es primo

def primo(n):
    contador = 1
    divisores = 0

    while contador <= n: # Número primo solo tiene dos divisiores, el uno y él mismo.
        if n % contador == 0:
            divisores += 1
        contador += 1
    if divisores == 2:
        print("El número ",n," es primo.")
    else:
        print("El número ",n," no es primo.")

numero = int(input("Ingrese un nùmero: "))

primo(numero)