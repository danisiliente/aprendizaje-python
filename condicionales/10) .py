#Solicite al usuario una cantidad numérica que expresa segundos (medida de 
#tiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso

segundos = int(input("Digite la cantidad de segundos a convertir"))
"""segPorHora = 3600
segPorMin = 60
if segundos > segPorHora:
    print("La cantidad es",round(segundos / segPorHora,1),"horas")
elif segundos > segPorMin:
    print("La cantidad es",round(segundos / segPorMin,1),"minutos")
else:
    print("La cantidad es",segundos,"segundos")"""
Horas = segundos // 3600
modMin = segundos % 3600
minutos = modMin // 60
segundos = modMin % 60

print("La cantidad en horas es: ",Horas)
print("La cantidad en minutos es: ",minutos)
print("La cantidad en segundos es: ",segundos)
