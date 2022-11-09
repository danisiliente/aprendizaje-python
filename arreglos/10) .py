#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Encuentre la desviación estandar

import random

tam=round(random.randint(5,10))

vec=[]
dif=[]
media=0

print('tam= ',tam)

for i in range (tam):
    vec.append(round(random.random()*100))
print(vec)

for i in vec:
    media+=i
media=media/len(vec)
print('media',media)

suma=0

for i in range(len(vec)):
    x=(vec[i]-media)**2
    dif.append(x)
    suma+=x
    
print('suma',suma)
print('desv estandar= ',(suma/len(vec))**0.5)
