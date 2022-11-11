def sumaDivisores(num):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma += i
    return suma

def perfectos(num):
    sum = sumaDivisores(num)
    if sum == num:
        return 'Perfecto'
    else:
        return 'Imperfecto'
    
print(perfectos(28))