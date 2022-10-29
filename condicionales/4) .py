# Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, 
# etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores.

nota = int(input("Digite la nota de 0 a 10 para saber cómo le fue: "))

if nota < 0:
    print("Nota inválida") 
elif nota < 3:
    print("Muy mal") # De 0 a 2 es muy mal.
elif nota < 5:
    print("Mal") # De 2 a 4 es mal.
elif nota < 7:
    print("Regular") # De 4 a 6 es regular.
elif nota < 9:
    print("Bien") # De 6 a 8 es bien.
elif nota < 11:
    print("Excelente") # De 8 a 10 es excelente.
else: 
    print("Nota inválida")

    

 