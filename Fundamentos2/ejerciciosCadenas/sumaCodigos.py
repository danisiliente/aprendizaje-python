# Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto.

def suma():
    cadena = input('Ingrese una cadena: ')

    cont = 0 

    for i in cadena:
        cont += (ord(i))

    print('La suma de los codigos es: ',cont)
    print('Valor numerico de acuerdo al alfabeto: ',chr(cont))

suma()