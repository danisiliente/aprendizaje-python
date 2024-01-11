class Aprendiz: # Se crea la clase Aprendiz.
    def __init__(self,nombre): # Se establece el constructor de la clase y recibe el parámetro nombre (self siempre debe estar).
        self.__nombre=nombre # El arumento que reciba de nombre, se almacenará en la variable privada __nombre.
        self.__cursos=[] # Se crea la variable privada __cursos y se le asigna una lista vacía.

    def agregarCurso(self,titulo): # Se crea la función encargada de agregar cursos, recibe el parámetro título (y self).
        self.__cursos.append(titulo) # El argumento recibido (titulo) se empezará a guardar en la lista de __cursos. 

    def getCursos(self): # GETTER.
        return self.__cursos # Retorna el valor de __cursos (la lista). 

class Curso: # Se crea la clase Curso.
    def __init__(self,titulo): # Se establece el constructor de la clase y recibe el parámetro título (además de self).
        self.__titulo=titulo # El arumento que reciba de titulo, se almacenará en la variable privada __titulo.

    def getTitulo(self): #GETTER.
        return self.__titulo # Retorna el valor de __titulo.
    
a=Aprendiz('Martha') # Se crea o instancia el objeto a de la clase Aprendiz. El argumento Martha activa el constructor.
c1=Curso('Python Intermedio') # Se crea o instancia el objeto c1 de la clase Curso y recibe el argumento de título.
c2=Curso('Python Basico') # Se crea o instancia el objeto c1 de la clase Curso y recibe el argumento de título.
c3=Curso('Introduccion a Java') # Se crea o instancia el objeto c1 de la clase Curso y recibe el argumento de título.

a.agregarCurso(c1) # El objeto a, utiliza el método para agregar el valor (curso) del objeto c1. Este método agrega a una lista el valor.
a.agregarCurso(c2) # El objeto a, utiliza el método para agregar el valor (curso) del objeto c2. Este método agrega a una lista el valor.
a.agregarCurso(c3) # El objeto a, utiliza el método para agregar el valor (curso) del objeto c3. Este método agrega a una lista el valor.

print(a.getCursos()) # Imprime los valores de la lista, o más bien un indicativo, ya que este getter no es el adecuado.

for curso in a.getCursos(): # Itera a través de la lista creada.
    print(curso.getTitulo()) # Imprime los valores de dicha lista con getter específico para eso.

#RETROALIMENTACIÓN: La composición es muy similar a la agregación, en este caso, al objeto aprendiz se le agregan objetos de la
#clase curso, pero sin necesidad de invocar una clase dentro de otra. No depende una de la otra.