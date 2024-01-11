import sqlite3 # Importa el módulo sqlite3 que ya viene por defecto en python.
with sqlite3.connect('conpython.db')as con: # Se utiliza un bloque de código al estilo de archivos, se realiza la conexión con una ruta relativa y se le asigna el alias de "con".
    micursor=con.cursor() # Crea el cursor, con la clase cursor(), que permite la manipulación de la base de datos.
    sentencia="SELECT nombre,apellido FROM alumno;" # Se le asigna una sentencia SQL a la variable "sentencia".
    print(micursor.execute(sentencia).fetchmany(10)) # Imprime la instrucción SQL por medio del cursor, se utiliza fetchmany para imprimir uno o varios elementos (en este caso 10).