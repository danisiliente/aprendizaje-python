import random

def ascendente(x,y):
    if x < y:
        return 'Ascendente'
    elif x > y:
        return 'Descendente'
    else:
        return 'Iguales'
    
'''num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
    
print(ascendente(x,y))'''    

for i in range(10):
    x = round(random.randrange(100))
    y = round(random.randrange(100))
    print(x,'-',y,' --> ',ascendente(x,y))
    
