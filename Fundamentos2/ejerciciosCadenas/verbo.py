# Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, 
# luego tres primeras y así sucesivamente hasta llegar a la última.

def imprimir_subcadenas(cad):
    control = len(cad)
    suma = 0
    for c in range(control - 1):
        sub = cad[:2 + suma]
        suma += 1
        print(sub)

imprimir_subcadenas('paralelismos')