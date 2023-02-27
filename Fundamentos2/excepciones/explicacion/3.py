def edad(): # Se define la función edad sin ningún argumento.
    try: # Aquí el código que puede generar una excepción.
        tuedad=int(input("introduce tu edad")) # Se solicita la edad del usuario como entero.
        print(f'tu edad es  {tuedad}') # Imprime la edad del usuario.
        #print('Tu edad es ',tuedad)
    except ValueError as e: # Excepción con el nombre del error como e.
        print(e) # Imprime el error.
        print("La edad debe ser un valor numerico...") # Imprime "la edad..."
        edad() # Llama de nuevo a la función.
    else: # De lo contrario (si la edad es un entero).
        print('Viene por el else') # Imprime el mensaje.

edad() # Llamado a la función.