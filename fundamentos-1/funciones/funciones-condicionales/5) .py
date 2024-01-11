#Solicite al usuario una cantidad numérica que expresa segundos (medida de 
#tiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso

def convertir(s):
    horas = s // 3600
    modMin = s % 3600
    minutos = modMin // 60
    s = modMin % 60
    print(horas,minutos,s)

segundos = int(input("Digite la cantidad de segundos a convertir: "))

convertir(segundos)