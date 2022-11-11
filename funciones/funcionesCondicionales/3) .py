#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número 
#exceda los límites emita un mensaje y finalice el programa.

def cifras(n):
    if n < 0 or n > 9999:
        return('El número está por fuera de los parámetros')
    else:
        return(len(n))
    
numero = int(input('Digite un número entre 0 y 9.999: '))
print(cifras(numero))
    