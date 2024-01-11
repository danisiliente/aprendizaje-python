#imprimir la raíz de 1 a n aleatorio.

import random

tam = round(random.random()*10)

vec = [(i+1)**0.5 for i in range(tam)] #vec = [round(random.random()*100)**0.5 for i in range(10)]

print(vec)