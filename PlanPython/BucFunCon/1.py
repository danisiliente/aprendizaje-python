#Deﬁne una función llamada raizCubica que devuelva el valor de raíz cúbica de n
#(Nota: recuerda que la notación raiz cubida de n, no es mas que una forma de expresar n**1/3) - pag 233

def raizCubica(n):
    print('La raíz cúbica de',n,'es: ',n ** (1 / 3))

while True:

    numero = int(input('Ingrese un número: '))
    if numero == 0:
        print('\nSEGUNDO EJERCICIO\n')
        break

    raizCubica(numero)

#Deﬁne una función llamada raiz que devuelva el valor de n raíz de x
#(Nota: recuerda que n raiz de x es x**(1/n)) - pag 242

def raiz(n,p):
    print('El número',n,'elevado a la',p,'es: ',n ** (1 / p))

while True:

    numero = int(input('Ingrese un número: '))
    potencia = int(input('Potencia a la que quiere elevar el número: '))
    if numero == 0:
        break

    raiz(numero,potencia)
