# Cuántas veces se repite un caracter dado.

texto = 'esto se repite, se repite'
caracter = 't'

def repetidos(t,c):

    contador = 0

    for x in t:
        if x == c:
            contador += 1
    return(contador)

print(repetidos(texto,caracter))