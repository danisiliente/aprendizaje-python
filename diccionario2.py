#clave - valor [] () {}

dict = {
    'gato':'cat',
    'perro':'dog',
    'vaca':'cow',
    'caballo':'horse'
}

#sorted() --> ordena el diccionario

print(dict)
print(dict.get('perro'))
print(dict['vaca'])

del dict['perro']
print(dict)

dict['raton'] = 'mouse'
print(dict)

dict.update({'perro':'dog'})
print(dict)

dict.popitem()#elimina el último
print(dict)

for i in dict.keys():#palabras clave
    print(i)
    
for i in dict.values():#valores
    print(i)
    
for k,v in dict.items(): 
    print(k,'-->',v)
    
for items in dict.items():
    print(items)