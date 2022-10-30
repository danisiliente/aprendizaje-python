#Algoritmo para hallar el m.c.d de dos números m y n por 
#el algoritmo de Euclides. 

primerNum = int(input("Ingrese el primer número: "))
segundoNum = int(input("Ingrese el segundo número: "))

#mcd = 0

while primerNum % segundoNum != 0: #Si el resultado es 0, el número menor es múltiplo del mayor.
    mcd = primerNum % segundoNum #En el algoritmo de Euclides se toma el mod y se vuelve a dividir hasta el mcd.
    primerNum = segundoNum
    segundoNum = mcd

print(segundoNum)
