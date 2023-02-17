# Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez.

def alfabeto(cad):
    cadena = ''
    for i in cad:
        if i not in cadena:
            cadena += i
    return len(cadena)

print(alfabeto('soacha'))