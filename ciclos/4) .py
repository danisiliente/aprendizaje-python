#Determinar cuales y cuantos números perfectos hay entre 1 y
#1000?

cont = 0

for n in range (1,1000,1):
    sumaDivisores = 0
    for i in range(1,n,1):
        if n % i == 0:
            sumaDivisores += i # Empieza en 0 y se van sumando los divisores
            
    if sumaDivisores == n:
        cont += 1
        print("El número ",n," es perfecto")
        
print("total de números perfectos: ",cont)

    
