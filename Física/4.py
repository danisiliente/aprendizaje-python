#ENERGÍA CINÉTICA --> EK = (m*(v**2))/2
#Calcule la energía cinética de un balón de 450g que fue pateado por Neymar a 80 m/s.

def calcCine(p,v):
    c = (p * (v) ** 2) / 2
    return round(c,1)

peso = 0.45
velocidad = 80

print(calcCine(peso,velocidad))