# Ingresar una palabra en minúscula y que esta se encripte con el cifrado Cesar.

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

# Cifrador de 3.

def cifrar(t):

    t = t.lower()

    letraCifrada = ''

    for letra in t:
        if letra in alfabeto:
            posicion = alfabeto.find(letra) # el método find encuentra el índice de cada letra
            posicion += 3
            if posicion >= 26:
                posicion -= 27
            letraCifrada += alfabeto[posicion]
        else:
            letraCifrada += letra

    print('Texto cifrado --> ',letraCifrada)

# Descifrador de 3.

def descifrar(t):

    t = t.lower()

    letraDescifrada = ''

    for letra in t:
        if letra in alfabeto:
            posicion = alfabeto.find(letra)
            posicion -= 3
            if posicion < 0:
                posicion += 27
            letraDescifrada += alfabeto[posicion]
        else:
            letraDescifrada += letra

    print(letraDescifrada)

# Abecedario Cesar (3).

def abecedario1():

    for letra in alfabeto:
        posicion = alfabeto.find(letra)
        posicion += 3
        if posicion >= 26:
            posicion -= 27
        print(letra,' --> ',alfabeto[posicion])

# Cifra con la diferencia de número que elija el usuario.

def cifradoCompuesto(t,n):

    t = t.lower()

    letraCifrada = ''

    for letra in t:
        if letra in alfabeto:
            posicion = alfabeto.find(letra)
            posicion += n
            if posicion >= 26:
                posicion -= 27
            letraCifrada += alfabeto[posicion]
        else:
            letraCifrada += letra

    print('Texto cifrado --> ',letraCifrada)

# Descifra con la diferencia de número que elija el usuario.

def descifradoCompuesto(t,n):

    t = t.lower()

    letraDescifrada = ''

    for letra in t:
        if letra in alfabeto:
            posicion = alfabeto.find(letra)
            posicion -= n
            if posicion < 0:
                posicion += 27
            letraDescifrada += alfabeto[posicion]
        else:
            letraDescifrada += letra

    print(letraDescifrada)

# Abecedario Cesar (número que elija el usuario).

def abecedario2(n):

    for letra in alfabeto:
        posicion = alfabeto.find(letra)
        posicion += n
        if posicion >= 26:
            posicion -= 27
        print(letra,' --> ',alfabeto[posicion])