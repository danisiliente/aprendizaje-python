class A1: # se crea la clase A1.
    def __init__(self): # Se establece el constructor de la clase (parámetro self que es obligatorio).
        pass # pass simula el código, es como si hubiera algo aquí y el intérprete siga normal su camino. 
    def saludo(self): # Se crea la función saludo (y self que es...).
        print('Hola desde A1') # Imprime el mensaje.

class A2: # se crea la clase A2.
    def __init__(self): # Se establece el constructor de la clase (parámetro self que es obligatorio).
        pass # pass simula el código, es como si hubiera algo aquí y...
    def saludo(self): # Se crea la función saludo (y self que es...).
        print('Hola desde A2') # Imprime el mensaje.


class B(A2,A1): # Se crea la subclase B con herencia multiple de A2 Y A1.
    def __init__(self): # Constructor de la clase (parámetro self que es obligatorio).
        pass # pass simula el código, es como si hubiera algo aquí y...
    def saludo(self): # Se crea la función saludo (y self que es...).
        print('Hola desde B') # Imprime el mensaje.
    def __str__(self): # Se crea la función str y su correspondiente self.
        return 'Soy un objeto de la clase B' # Instrucción para que retorne el mensaje.
    
obj=B() # Se crea o instancia el objeto de la clase B.
print(obj.__str__()) # Imprime "Soy un objeto..." recordar que la herencia empieza desde la clase misma hacia arriba y según como se haya pasado (izquierda a derecha).
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())