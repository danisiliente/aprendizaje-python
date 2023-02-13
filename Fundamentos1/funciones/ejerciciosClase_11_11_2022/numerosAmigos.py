def sumaDivisores(num):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma += i
    return suma

def amigos(a,b):
    if sumaDivisores(a) == b and sumaDivisores(b) == a:
        return 'amigos'
    else:
        return 'No amigos'

print(amigos(220,284))