#Escriba un programa que resuelva la fórmula cuadrática, dados 3 números.
#a*x**2+b*x+c=0
#FÓRMULA G: x = -b +- raíz b** - 4*a*c / 2*a

from math import sqrt
while True:
    def cuadratica():
        res = []
        try:
            a = int(input("Digite el primer valor: "))
            b = int(input("Digite el segundo valor: "))
            c = int(input("Digite el tercer valor: "))
            x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
            x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
            res.append([x1,x2])
            print('la solución de la eciación es:', res)
        except ZeroDivisionError:
            print('No se puede realizar la división por 0')
        except ValueError:
            print('Esta ecuación es demasiado compleja')
        except:
            print('No sé qué otro error hay, pero está mal.')
    cuadratica()