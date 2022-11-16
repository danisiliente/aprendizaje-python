#Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan 
#200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que 
#permita calcular el costo de una llamada dados los minutos de duración.

def costo(m):
    if m <= 3:
        print('costo: $', m * 200) 
    else:
        print('costo: $',m * 250 - 150)
    
minutos = int(input('Ingrese los minutos de la llamada: '))
costo(minutos)