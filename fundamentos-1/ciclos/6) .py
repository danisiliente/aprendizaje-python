#Calcular el máximo de números positivos introducidos por 
#teclado, sabiendo que metemos números hasta que 
#introduzcamos uno negativo. El negativo no cuenta. 

primerNumero = int(input("Ingrese un número: "))

numerosPositivos = 0

#if primerNumero > 0:
while primerNumero > 0:
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        numerosPositivos += 1
    else:
        break
print("Usted ingresó ",numerosPositivos + 1," números positivos")
#else:
    #print("Error 404.")




