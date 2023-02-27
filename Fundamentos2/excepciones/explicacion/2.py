def try_syntax(numerator, denominator): # Se crea una función y se le pasan dos parámetros.
    try: # Aquí el código que puede generar una excepción.
        print(f'In the try block: {numerator}/{denominator}') # Imprime un mensaje mostrando el numerador y denominador.
        result = numerator / denominator # Variable que almacena la división.
    except ZeroDivisionError as zde: # Se define la excepción con el tipo de error como zde.
        print(zde) # Imprime el error.
    else: # De lo contrario.
        print('The result is:', result) # Imprime el resultado
        return result 
    finally: # Lo que va aquí siempre saldrá.
        print('Exiting...') # Imprime "saliendo..."
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 0)) # Se invoca a la función y se le pasan los dos argumentos.