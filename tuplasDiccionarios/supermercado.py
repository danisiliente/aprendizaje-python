#agregar productos como si fuera una caja registradora. Mostrar el promedio, cuál es el más caro y el más barato por cliente.

productos = {}

while True:
    name = input("Ingresa el nombre del cliente: ")
    if name == '':
        break
    
    precio = int(input("Ingresa el precio del producto $ "))
    if precio not in range(0,100001):
	    break
    
    if name in productos:
        productos[name] += (precio,)
    else:
        productos[name] = (precio,)
              
for name in sorted(productos.keys()):
    adding = 0
    counter = 0
    for score in productos[name]:
        adding += score
        counter += 1
    print('Promedio de ',name, ":", adding / counter)
    print('Precio todal de ',name,adding) 
    
    

    
    