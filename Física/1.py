#ENERGÍA CINÉTICA --> EK = (m*(v**2))/2
#Si Messi patea un balón de 450g con una velocidad de 62.6 km/h y mete gol, digite la energía cinética del balón. 

print('⚽Si Messi (Goat) patea un balón de 450g con una velocidad de 62.6 km/h y mete gol, digite la energía cinética del balón.⚽\nFórmula --> EK = (m*(v**2))/2')

def cinetica(u):
    if u > 66 and u < 71:
        print('Correcto --> El fifas')
        exit()
    else:
        print('Incorrecto')
        
m = 0.45
v = 17.38

ek = (m*(v)**2)/2

while True:
    u = float(input('Digite la energía cinética del balón: '))
    cinetica(u)