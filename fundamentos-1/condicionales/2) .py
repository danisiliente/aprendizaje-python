#Solicite al usuario la temperatura en grados celsius y conviértala a farenheit, kelvin y rankine.

c=int(input("digite cnatidad de grados celsius"))
f=(c*(9/5))+32
k=(c+273.15)
r=(c*(9/5))+491.67

print(c,' grados celsius equivalen a ',f,' grados farenheit, a ',k,' grados kelvin y a',r,' grados rankine.')