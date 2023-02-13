#num aleatorios = edad, imprimir si es mayor de edad o menor de edad.

import random

vec = [round(random.random()*100) for i in range(10)]
print(vec)

num = ['mayor' if x >= 18 else 'menor' for x in vec]
print(num)