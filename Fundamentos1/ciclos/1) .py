#Determinar los divisores de un número introducido por
#teclado

numero = int(input("Introduzca un número: "))

contador = 0

for i in range(1,numero,1): 

    if (numero % i) == 0: # Los divisores no dejan residuo

        print(i,"es divisor de ",numero)

        contador += 1

print("el número ",numero," tiene ",contador," divisores.")

 