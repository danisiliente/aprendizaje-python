# Solicite una cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas.

cadena = input('Ingrese un texto: ')

def formas(t):
    print(t.lower())
    print(t.upper())
    print(t.title())
    print(t.swapcase())
    print(t.capitalize())
    print(t.casefold())

formas(cadena)