# Escribe un programa que pida tres números y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos.

def iguales(a,b,c):
    if a == b == c:
        return"hay tres números iguales"
    elif a == b or a == c or b == c:
        return"Hay dos números iguales"
    else:
        return("Los tres números son distintos")
    
num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo número"))
num3 = int(input("Digite el tercer número"))

print(iguales(num1,num2,num3))