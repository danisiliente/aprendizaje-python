#¿Cuáles y cuántos son los números primos comprendidos
#entre 1 y 1000?

numero = 1

while numero <= 1000:
    contador = 1
    divisores = 0

    while contador <= numero:
        if numero % contador == 0:
            divisores += 1
        contador += 1

    if divisores == 2:
        print(numero)

    numero += 1
    