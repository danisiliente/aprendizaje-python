#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña
#y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
#hacer login incremente este valor.
#https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u37/

def login(nom,con):
	if nom == "sena" and con == "cide":
		print('¡Usuario y contraseña correcta!')
	else:
		print('incorrecto')

intentos = 0

while intentos < 3:
    usuario = input("Digite el nombre de usuario: ")
    clave = input("Digite la contraseña: ")
    login(usuario,clave)
    intentos += 1