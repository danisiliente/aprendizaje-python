#Solicitar 2 números al usuario e imprimir el cociente y el 
#residuo del mayor en el menor sin utilizar la división ni el mod. 

dividendo = int(input("Ingrese el primer número (dividendo): "))
divisor = int(input("Ingrese el segundo número (divisor): "))

cociente = 0

while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1
    
print("El residuo es: ", dividendo)
print("El cociente es: ",cociente)