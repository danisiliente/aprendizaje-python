# Cree un programa que calcule el Área, longitud, diámetro y circunferencia de un círculo.

def calcTriangulo(r):
    area = 3.14 * radio ** 2 # a = pi * r**2
    longitud = 2 * 3.14 * radio # l = 2*pi*r
    diametro = 2 * radio # d = 2*r
    circunferencia = diametro * 3.14 # c = d*pi
    return area,longitud,diametro,circunferencia

radio = float(input("Escriba el Radio del círculo: "))
print(calcTriangulo(radio))