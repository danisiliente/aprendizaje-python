# Escribe un programa que pida tres números y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos.

num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo número"))
num3 = int(input("Digite el tercer número"))

if num1 == num2 == num3:
    print("hay tres números iguales")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Hay dos números iguales")
else:
    print("Los tres números son distintos")