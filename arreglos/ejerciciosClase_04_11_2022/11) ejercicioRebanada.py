#calcular la temperatura promedio, promedio de la primera mitad y promedio de los tercios.
import random

#temp=random.randint(5,28)

mes = [random.randint(5,28) for i in range(1,31)]

print(mes)
m1 = mes[:15]
m2 = mes[15:-1]
t1 = mes[:11]

s = 0

for i in m1:
    s += i
print('promedio:',s/len(m1))

for i in m2:
    s += i
print('promedio:',s/len(m2))

for i in t1:
    s += i
print('promedio:',s/len(t1))