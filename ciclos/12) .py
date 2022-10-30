"""Escribir un programa que visualice la siguiente figura, 
utilizando ciclos. El usuario decide cuantas líneas quiere 
imprimir 
* 
* * 
* * * 
* * * *"""

cantidad = int(input("Digite la cantidad de líneas a imprimir: "))

for i in range(cantidad):
    print("*" * (i + 1))
