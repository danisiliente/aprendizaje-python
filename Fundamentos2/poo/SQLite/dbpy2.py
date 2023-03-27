import sqlite3 # Importa el módulo sqlite3 que ya viene por defecto en python.

with sqlite3.connect('conpython.db')as con: # Se utiliza un bloque de código al estilo de archivos, se realiza la conexión con una ruta relativa y se le asigna el alias de "con".
    micursor=con.cursor() # Crea el cursor, con la clase cursor(), que permite la manipulación de la base de datos.
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;" # Se le asigna una sentencia SQL a la variable "sentencia".
    #print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato): # Se crea la función "miselect" y se le asignan 5 atributos.
    micursor=conexion.cursor() # Crea el cursor, con la clase cursor(), que permite la manipulación de la base de datos.
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'" # Se crea la sentencia en una plantilla literal y recibe algunos de los argumentos.
    print(sentencia) # Imprime sentencia como un string.
    print(micursor.execute(sentencia).fetchall()) # Imprime la instrucción dada en sentencia con los argumentos pasados.

miselect(con,'alumno','email','=','dbrabon2@irs.gov') # Se invoca a la función y se le pasan los 5 argumentos.

def modificar(conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo} = '{dato}' WHERE id='{id}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación exitosa !!!!')
    
#modificar(con,'alumno','nombre','vegetita',1)
#DELETE FROM table_name WHERE condition;

def eliminar(conexion,tabla,campo,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación exitosa, gonorrea !!!!')