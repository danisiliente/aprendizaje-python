class Curso: # Se crea la clase curso.
    def __init__(self,titulo): # Se establece el constructor de la clase con el parámetro self (obligatorio) y título.
        self.__titulo=titulo # El arumento que reciba de título, se almacenará en la variable privada __titulo.

    def getTitulo(self): # GETTER.
        return self.__titulo # Retorna el valor de la variable privada __titulo. 

class Aprendiz: # Se crea la  clase aprendíz.
    def __init__(self,nombre): # Se establece el constructor de la clase con el parámetro self (obligatorio) y nombre.
        self.__nombre=nombre # El arumento que reciba de nombre, se almacenará en la variable privada __nombre.
        self.__cursos=[] # Se crea la variable privada __cursos y se le asigna una lista vacía.

    def agregarCurso(self,nombreCursito): # Se crea la función que se encargará de agregar el nombre del curso.
        cursito=Curso(nombreCursito) # la variable cursito llama a la clase Curso y se le pasa el argumento que recibe como nombre del curso (esto activa el constructor).
        self.__cursos.append(cursito) # La lista vacía de la variable privada __cursos, se empezará a llenar con el nombre de los cursos.

    def getCursos(self): #GETTER.
        return self.__cursos # Retorna los valores de __cursos (la lista).
    
ap=Aprendiz('Sofia') # Se crea o instancia el objeto ap de la clase Aprendíz. El argumento Sofía activa el constructor.
ap.agregarCurso('Python Basico') # Se invoca el método para agregar curso y se le da como argumento en nombre del curso.
ap.agregarCurso('Python Intermedio') # Se invoca el método para agregar curso y se le da como argumento en nombre del curso.

for c in ap.getCursos(): # El bucle va a iterar en todos los cursos que tenga el objeto ap en su getter (cada valor).
    print(c.getTitulo()) # Imprime el nombre de cada valor encontrado, haciendo uso del getter de la clase título.

#RETROALIMENTACIÓN: La agregación sucede en el momento en que al objeto de la clase aprendíz, se le agregan valores (cursos)
#de objetos que pertenecen a otra clase, es por eso que en la función de agregar curso (en la clase Aprendíz), se invoca a la clase Curso.
#¿Esta invocación hace que dependa una de la otra?