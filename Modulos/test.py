import daniel

texto1 = input('Ingrese el texto que desea cifrar: ')

daniel.cifrar(texto1) # Cifra el texto con el método Cesar (3).

texto2 = input('Ingrese el texto que desea descifrar: ')

daniel.descifrar(texto2) # Descifra el texto (método Cesar), se recomienda copiar y pegar el texto cifrado (3).

var1 = input('¿Desea ver el abecedario Cesar? --> s/n: ')
var1 = var1.lower()

if var1 == 's':
    daniel.abecedario1() # Muestra el abecedario Cesar (3).

texto3 = input('Ingrese el texto que desea cifrar: ')
numero = int(input('Ingrese el número de diferencia con el que desea encriptar: '))

daniel.cifradoCompuesto(texto3,numero) # Cifra el texto (método Cesar) con la diferencia numerica que dé el usuario.

texto4 = input('Ingrese el texto que desea descifrar: ')

daniel.descifradoCompuesto(texto4,numero) # Descifra el texto (método Cesar), se recomienda copiar y pegar el texto cifrado (n).

var2 = input('¿Desea ver el abecedario Cesar utilizado? --> s/n: ')
var2 = var2.lower()

if var2 == 's':
    daniel.abecedario2(numero) # Muestra el abecedario Cesar (n).