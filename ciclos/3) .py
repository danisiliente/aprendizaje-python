#Determinar si un número es o no es perfecto. Un numero es
#perfecto si la suma de sus divisores sin incluir el propio
#número es igual a este

numero = int(input("Ingrese un nùmero: "))

sumaDivisores = 0

for i in range(1,numero,1):
    if numero % i == 0:
        sumaDivisores += i # Empieza en 0 y se van sumando los divisores
        
if sumaDivisores == numero:
    print("El número ",numero," es perfecto")
else:
    print("El número ",numero," no es perfecto")