#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el 
#valor del medio es 11. No use operadores lógicos

num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo número"))
num3 = int(input("Digite el tercer número"))

numeroMenor = min(num1,num2,num3)
numeroMayor = max(num1,num2,num3)

numeroMedio = (num1 + num2 + num3) - numeroMayor - numeroMenor

print("El número del medio es: ",numeroMedio)