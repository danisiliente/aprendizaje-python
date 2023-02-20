#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.

def contarVocales(cad):
    vocales = 0
    consonantes = 0
    vocalesConTilde = 0
    caracterE = 0
    
    cad = cad.lower()
    
    for c in cad:
        if c.isalpha():
            if c in "aeiou":
                vocales += 1
            elif c in "áéíóú":
                vocalesConTilde += 1
            else:
                consonantes += 1
          
        if c not in "abcdefghijklmnñopqrstuvwxyzáéíóú":
            caracterE += 1

    print(vocales,consonantes,vocalesConTilde,caracterE)

contarVocales('agúa!!_')