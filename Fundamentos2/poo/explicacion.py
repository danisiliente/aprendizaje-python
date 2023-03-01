class Persona: # Se define la clase con el nombre Persona.
    def __init__(self,nombre): # Se crea la función __init__ o constructor, se le pasan dos parámetros: self (que es obligatorio) y nombre.
        self.__nombre=nombre # Se crea la variable __nombre (privada), se antepone self para especificar que es de "aquí mismo" y se le asigna nombre.
        print('Activando constructor') # Imprime el mensaje.

    def getNombre(self): # Se crea la función getNombre con el parámetro obligatorio self.
        return self.__nombre # GETTER: Retorna el nombre que se le ha pasado como argumento a la variable privada __nombre. (Solo accede al valor, no a la variable.)

    def setNombre(self, nombre): # Se crea la función setNombre con el parámetro obligatorio self y, además, el parámetro que se desea implementar en la modificación.
        self.__nombre=nombre # SETTER: Modifica el valor que estaba en la variable privada __nombre.

    def metodo(self): # Se crea la función metodo con el parámetro obligatorio self.
        print('Soy un método') # Imprime el mensaje.

ob=Persona('Ana') # Se instancia el objeto ob de la clase Persona. (Siempre primera letra es mayúscula en el nombre de la clase.)
print(ob.getNombre()) # Imprime el nombre, llamando a la función getNombre y anteponiendo el nombre del objeto, seguido por un punto.
ob.setNombre('Maria') # Se le da el argumento para realizar la modificación del valor almacenado en __nombre.
print(ob.getNombre()) # Imprime el nuevo nombre, llamando a la función getNombre y anteponiendo el nombre del objeto, seguido por un punto.
#ob.metodo()
#print(type(ob))