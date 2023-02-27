values = (1, 0) # Se crea una tupla en values.

#x,y=19,30
#print(divmod(10,3))

try: # Aquí se coloca el código que podría generar una excepción.
    q, r = divmod(*values) # Se crean dos variables y la función divmod traerá el cociente y residuo de la división a/b de values.
    #print('q=',q)
    print(f'q={q}') # Imprime el cociente. 
    print(f'r={r}') # Imprime el residuo.
except (ZeroDivisionError, TypeError) as e: # Aquí se definen los tipos de errores como e.
    print(type(e), e) # Imprime el tipo de error y el error.