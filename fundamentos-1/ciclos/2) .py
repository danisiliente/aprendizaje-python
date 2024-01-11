#Determinar si un numero es o no es primo

numero = int(input("Ingrese un nùmero: "))

contador = 1
divisores = 0

while contador <= numero: # Número primo solo tiene dos divisiores, el uno y él mismo.
    if numero % contador == 0:
        divisores += 1
    contador += 1
if divisores == 2:
    print("El número ",numero," es primo.")
else:
    print("El número ",numero," no es primo.")