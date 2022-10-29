#Solicite dos números fraccionarios conformados por numerador y denominador, muestre la suma, resta, multiplicación y división.

num1 = int(input("Digite el numerador del primer fraccionario"))
den1 = int(input("Digite el denominador del primer fraccionario"))
num2 = int(input("Digite el numerador del segundo fraccionario"))
den2 = int(input("Digite el denominador del segundo fraccionario"))

print("Números fraccionarios: ","(",num1,"/",den1,")","(",num2,"/",den2,")")

suma = (num1*den2 + den1*num2) / (den1*den2)
resta = (num1*den2 - den1*num2) / (den1*den2)
multiplicacion = (num1*num2) / (den1*den2)
division = (num1*den2) / (den1*num2)

print("La suma de sus fraccionarios es: ",suma)
print("La resta de sus fraccionarios es: ",resta)
print("La multiplicación de sus fraccionarios es: ",multiplicacion)
print("La división de sus fraccionarios es: ",division)
