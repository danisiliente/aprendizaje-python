#Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan 
#200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que 
#permita calcular el costo de una llamada dados los minutos de duración.

minutos = int(input("Digite la cantidad de minutos"))

if minutos < 3:
    print("El costo de sus minutos es:",minutos * 200,"pesos")
else:
    print("El costo de sus minutos es:",minutos * 250 - 150,"pesos")
