# Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.

# Cifrador de 3.

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

texto = 'bienvenido a las cadenas'

def cifrar(t):

    t = t.lower()

    letraCifrada = ''

    for letra in t:
        if letra in alfabeto:
            posicion = alfabeto.find(letra) # el método find encuentra el índice de cada letra
            posicion += 1
            if posicion >= 26:
                posicion -= 27
            letraCifrada += alfabeto[posicion]
        else:
            letraCifrada += letra

    print('Texto cifrado --> ',letraCifrada)

cifrar(texto)