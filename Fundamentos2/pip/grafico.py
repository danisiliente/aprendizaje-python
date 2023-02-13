from matplotlib import pyplot

trimestres = [1,2,3,4,5,6,7]
dificultad = [100,1250,8500,19000,39000,70000,100000]
pyplot.plot(trimestres, dificultad)

dificultad2 = [150,1550,10500,24000,45000,85000,120000]
pyplot.plot(trimestres, dificultad2)

pyplot.xlabel('Trimestres')
pyplot.ylabel('Nivel de dificultad')
pyplot.title('Dificultad de los trimestres en ADSO')
pyplot.legend(['Estudiantes SENA','Estudiantes SENA de Soacha'])
pyplot.show()