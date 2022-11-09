#Haga una función que reciba la temperatura en celsius y la devuelva en farenheit, kelvin y Rankine

def conversion(n):
    f = (n*(9/5))+32
    k = (n+273.15)
    r = (n*(9/5))+491.67
    print(n,'Grados celsius equivalen a:\n''Farenheit:',f,'Kelvin:',k,'Rankine:',r)
    
conversion(5)
    
'''c=int(input("digite cnatidad de grados celsius"))
f=(c*(9/5))+32
k=(c+273.15)
r=(c*(9/5))+491.67

print(c,' grados celsius equivalen a ',f,' grados farenheit, a ',k,' grados kelvin y a',r,' grados rankine.')'''