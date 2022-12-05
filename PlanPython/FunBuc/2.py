#Deﬁne una función que convierta grados Farenheit en grados Celsius 
#(Para calcular los grados Celsius debes restar 32 a los grados Farenheit
#y multiplicar el resultado por cinco novenos). - pag 233

def farenAcenti():
    f = float(input('\nIngrese grados Farenheit para convertirlos a Celsius: '))
    c = round((f - 32) * 5/9,1)
    print(f,'grados Farenheit, son:',c,'grados Celsius.\n')
 
#Deﬁne una funcion que convierta grados Celsius en grados Farenheit 

def centiAfaren():
    c = float(input('Ingrese grados Celsius para convertirlos a Farenheit: '))
    f = round((c * 9 / 5) + 32,1)
    print(c,'grados Celsius, son:',f,'grados Farenheit.\n')

#Deﬁne una funcion que convierta radianes en grados (Recuerda que 360 grados son 271 radianes)

def radianAgrado():
    r = float(input('Ingrese los Radianes que quiere convertír a Grados: '))
    g = round(r * (180 / 3.14),1) #Fórmula radian --> grado
    print('La conversión de',r,'Radianes a Grados, es:',g,'\n')

#Deﬁne una funcion que convierta grados en radianes

def gradoAradian():
    g = float(input('Ingrese los Radianes que quiere convertír a Grados: '))
    r = round(g * (3.14 / 180),1) #Fórmula grado --> radian
    print('La conversión de',g,'Grados a Radianes, es:',r)

farenAcenti()
centiAfaren()
radianAgrado()
gradoAradian()