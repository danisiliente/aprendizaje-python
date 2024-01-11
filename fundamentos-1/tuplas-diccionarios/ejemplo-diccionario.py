pc = {'ram':16,'procesador':8,'vc':6,'ssd':1000,'fuente':650}
print(pc)
print(pc['procesador'])
print(pc['ram'],pc['ssd'])
del pc['ram']
print(pc)
for objeto, valor in pc.items():
    print('en la pc tenemos',objeto,valor)

pc['board'] = 'Asus b520'
print(pc)