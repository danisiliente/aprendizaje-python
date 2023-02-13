#Escribe un programa que inicie mostrando en pantalla la letra de “Un elefante se balanceaba” 
#iniciando con el número 1, después pregunta al usuario cuantos elefantes más se balancearán
#y debe responder un número más al mostrado. En caso de ingresar un número diferente pedirle 
#que intente de nuevo y repetir el ciclo hasta tener 10 elefantes.
#Tomar en cuenta cuando el texto muestra un solo elefante y varios elefantes.
#https://platzi.com/comunidad/retos-de-programacion-en-cualquier-lenguaje-sexto-nivel-ciclo-while-2/

import random

print('\nUn elefante se balanceaba sobre la tela de una araña.')
print('Como la tela se resistía, fueron a llamar más elefantes... \n')

def bucle(n,a):
    if n != a:
        print('\n',n,'elefantes se balanceaban sobre la tela de una araña.')
        print('Como la tela se resistía, fueron a llamar más elefantes... \n')
    else:
        print('Ya no resistió.')
        exit()

elefantes = random.randint(1,100)

while True:
    num = int(input('Cuántos elefantes se podran balancear antes de que se rompa la tela: '))
    bucle(num,elefantes)