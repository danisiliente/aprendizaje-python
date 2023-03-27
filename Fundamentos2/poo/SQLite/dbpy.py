import sqlite3 # Importa el módulo sqlite3 que ya viene por defecto en python.
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
con=sqlite3.connect('conpython.db') # Realiza la conexión con la base de datos, la ruta puede ser absoluta o relativa.
print(type(con)) # Imprime el tipo de dato de la conexión.
micursor=con.cursor() # Crea el cursor, con la clase cursor(), que permite la manipulación de la base de datos.
print(type(micursor)) # Imprime el tipo de cursor. 
sentencia="SELECT * from alumno;" # Se le asigna una sentencia SQL a la variable "sentencia".
micursor.execute(sentencia) # Se ejecuta la sentencia SQL, haciendo uso del cursor y la función execute(con la sentencia).
for fila in micursor.fetchall(): # Itera a través los datos traídos con el cursor y hace uso de la función fetchall() que trae todos los datos que encuentre.
    print(fila[0]) # Imprime la posición 0 de la fila iterada.
    print(fila[1]) # Imprime la posición 1 de la fila iterada.
    print(fila[2]) # Imprime la posición 2 de la fila iterada.
    print(fila[3]) # Imprime la posición 3 de la fila iterada.
    print('-'*50) # Imprime 50 guiones que funcionan como separador.