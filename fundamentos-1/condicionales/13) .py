# Cree un programa que calcule el Área, longitud, diámetro y circunferencia de un círculo.

radio = float(input("Escriba el Radio del círculo: "))
area = 3.14 * radio ** 2 # a = pi * r**2
longitud = 2 * 3.14 * radio # l = 2*pi*r
diametro = 2 * radio # d = 2*r
circunferencia = diametro * 3.14 # c = d*pi
print("El Área del círculo es: ", area)
print("La longitud del círculo es: ", round(longitud,1))
print("El diámetro del círculo es: ", diametro)
print("La circunferencia del círculo es: ", round(circunferencia))



