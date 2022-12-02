#TRABAJO W = F*d*cos(a)
#Si aguatero mueve un petaco de agua con una varilla a una distancia horizontal de 5m, con un ángulo de 21° con respecto al piso, si la tensión
#de la varilla es de 12 N, digite el trabajo realizado.

import math

print('🍺Si aguatero mueve un petaco de agua con una varilla a una distancia horizontal de 5m, con un ángulo de 21° con respecto al piso, si la tensión🍺\nFórmula --> F*d*cos(a)')

'''def trabajo(u):
    if u > 75 and u < 80:
        print('Correcto --> El fifas')
        exit()
    else:
        print('Incorrecto')'''
        
f = 6
d = 15
a = 30

w = (f*d)*math.cos((3.1416)*a)

print(w)

'''while True:
    u = float(input('Digite el trabajo realizado: '))
    trabajo(u)'''