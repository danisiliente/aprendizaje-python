"""Escribir un programa que visualice la siguiente figura, 
utilizando ciclos. El usuario decide cuantas líneas quiere 
imprimir 
* 
* * 
* * * 
* * * *"""

def figura(n):
    for i in range(n):
        print("*" * (i + 1))
    
numero = int(input('Ingrese la cantidad de filas de la figura: '))

print(figura(numero))