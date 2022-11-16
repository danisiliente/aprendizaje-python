# Escribe un programa que pida tres números y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos.

def iguales(a,b,c):
    if a == b == c:
        print("hay tres números iguales")
    elif a == b or a == c or b == c:
        print("Hay dos números iguales")
    else:
        print("Los tres números son distintos")
    
num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número: "))
num3 = int(input("Digite el tercer número: "))

iguales(num1,num2,num3)