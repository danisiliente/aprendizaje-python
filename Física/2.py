#ENERGÍA POTENCIAL --> EP = m*g*h
#Si critiano ronaldo salta a 2.56 m de altura y cabecea un balón de 450g (y mete gol), digite la energía potencial del balón en relación con el piso

print('⚽Si critiano ronaldo salta a 2.56 m de altura y cabecea un balón de 450g (y mete gol), digite la energía potencial del balón en relación con el piso⚽\nFórmula --> EP = m*g*h\ng = 9.8')

def potencial(u):
    if u > 9 and u < 13:
        print('Correcto --> El fifas')
        exit()
    else:
        print('Incorrecto')
        
m = 0.45
h = 2.56
g = 9.8

ep = (m)*(g)*(h)

while True:
    u = float(input('Digite la energía potencial del balón: '))
    potencial(u)