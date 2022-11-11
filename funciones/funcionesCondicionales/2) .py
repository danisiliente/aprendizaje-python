#Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan 
#200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que 
#permita calcular el costo de una llamada dados los minutos de duración.

def costo(m):
    if m <= 3:
        return m * 200
    else:
        return m * 250 - 150
    
minutos = int(input('Ingrese los minutos de la llamada: '))
print('costo: ',costo(minutos))