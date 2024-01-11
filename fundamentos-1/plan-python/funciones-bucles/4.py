#Generar una tabla de multiplicar.
#https://altocodigo.blogspot.com/p/aprender-haciendo.html

def tabla(num,mul):
    for i in range(1,mul + 1,1):
        mul = num * i
        print(num,'x',i,'-->',mul)

while True:
    numero = int(input('\nDigite el número que quiere multiplicar: '))
    if numero == 0:
        break
    valor = int(input('Hasta qué número lo quiere multiplicar: '))

    tabla(numero,valor)