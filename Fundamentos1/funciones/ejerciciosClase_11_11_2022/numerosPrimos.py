def sumaDivisores(num):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma += i
    return suma

def primos(num):
    sum = sumaDivisores(num)
    if sum == 1:
        return 'Es primo'
    else:
        'No es primo'

print(primos(11))