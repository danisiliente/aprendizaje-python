#Construir un pequeño programa que convierta números binarios en enteros.

def decBin(n,l):
    while n != 0:
        mod = n % 2
        cociente = n // 2
        l.append(mod)
        l.reverse()
        n = cociente
    print(l)

def binDec(n):
    sum = 0
    pos = 0
    while n >= 1:
        dig = n % 10
        n = n // 10
        sum += dig * (2 ** pos)
        pos += 1
    print(sum)

binarios = []

opcion = input('¿Decimal a Binario o Binario a Decimal? 1 o 2: ')

if opcion == '1':
    numero = int(input('Ingrese un número entero: '))
    decBin(numero,binarios)
elif opcion == '2':
    numero = int(input('Ingrese un número Binario: '))
    binDec(numero)
else:
    print('No válido')