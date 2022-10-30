#Determinar cuales son los múltiplos de 5 comprendidos entre 
#1 y N. 

numero = int(input("Digite un número: ")) # Número máximo N

#multiplos = 0

for i in range(1,numero + 1,1):
    if i % 5 == 0:
        print(i)
    