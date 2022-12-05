#Deﬁne una función que, dado el valor de los tres lados de un triangulo, 
#devuelva la longitud de su perímetro. - pag 242

def tri(a,b,c):
    print('La longitud del perímetro es: ',a+b+c) 

lado1 = int(input('ingrese el primer lado del triángulo: '))

lado2 = int(input('ingrese el segundo lado del triángulo: '))

lado3 = int(input('ingrese el tercer lado del triángulo: '))

tri(lado1,lado2,lado3)

#Deﬁne una función llamada areaicírculo que, a partir del radio de un círculo, 
#devuelva el valor de su área. Utiliza el valor 3.1416 como aproximación de pi 
#o importa el valor de pi que encontrarás en el módulo math.
#(Recuerda que el área de un círculo de radio r es pi*(r**2)) - pag 233

def areaCirculo(r):
    print('El área del círculo es: ',3.14 * (r ** 2)) 

while True:

    radio = int(input('\nIngrese el radio del círculo: '))
    if radio == 0:
        break

    areaCirculo(radio)