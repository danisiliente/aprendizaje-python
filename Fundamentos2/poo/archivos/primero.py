# with open('texto.txt', 'a') as archivo:
#     archivo.write('\nHola fulanos')
    
# with open('texto.txt', 'r') as archivo:
#     print(archivo.readlines())
    
# with open('texto.txt', 'r+') as archivo:
    # print(archivo.read())
    # archivo.write('\nHola fulanos2')
    
# with open('texto.txt', 'w+') as archivo:
#     archivo.write('Hola')
    
with open('texto.txt', 'r') as archivo:
    for x in archivo:
        print(x)