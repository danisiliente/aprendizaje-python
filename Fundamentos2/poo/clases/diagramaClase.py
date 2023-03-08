class registrar:
    def __init__(self, documento, nombre, edad, telefono, rol, nomUsuario, contraseña):
        self.documento = documento
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.rol = rol
        self.__nomUsuario = nomUsuario
        self.__contraseña = contraseña
        self.profesores = {}
        self.estudiantes = {}

    def añadirUsuario(self):
        if self.rol == 'estudiante':
            self.estudiantes = {'Nombre':self.nombre,'Rol':self.rol}
        elif self.rol == 'profesor':
            self.profesores = {'Nombre':self.nombre,'Rol':self.rol}
        else:
            print('Rol no admitido')

    def setActualizar(self, edad, telefono, nomUsuario, contraseña):
        self.edad = edad
        self.telefono = telefono
        self.__nomUsuario = nomUsuario
        self.__contraseña = contraseña

    def getMostrarEst(self): # No está en el diagrama
        return self.estudiantes

    def getMostrarPro(self):
        return self.profesores
    
#-------------------------------------------------------------------------------------

class profesores(registrar):
    pass

#-------------------------------------------------------------------------------------

class estudiantes(registrar):
    pass

#-------------------------------------------------------------------------------------

class materias:
    def __init__(self, id, nombre, descripcion, horario):
        self.__id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.horario = horario
        self.profesor = []

    def añadirProf(self, profesor):
        self.profesor.append(profesor)

    def getMostrarMat(self):
        return self.nombre, self.profesor
    
#-------------------------------------------------------------------------------------
    
class curso:
    def __init__(self, id, descripcion, fecha, nivel):
        self.__id = id
        self.descripcion = descripcion
        self.fecha = fecha
        self.nivel = nivel
        self.materias = []

    def agregarMat(self, materia):
        mate = materia  
        self.materias.append(mate)

    def setActualizar(self, descripcion, fecha, nivel):
        self.descripcion = descripcion
        self.fecha = fecha
        self.nivel = nivel

    def getMostrarCur(self):
        print(f'Curso {self.descripcion}', self.materias)

#-------------------------------------------------------------------------------------

estudiante1 = registrar(12345, 'Fabrizio', '19', '3002345890', 'estudiante', 'Fab1', '12345')
estudiante1.añadirUsuario()
print(estudiante1.getMostrarEst())

profesor1 = profesores(67890, 'Francesco', '39', '3224507633', 'profesor', 'Fran3', '67890')
profesor1.añadirUsuario()
print(profesor1.getMostrarPro())

profesor2 = profesores(101112, 'Facundo', '42', '3234508800', 'profesor', 'Facu4', '101112')
profesor2.añadirUsuario()
print(profesor2.getMostrarPro())

materia1 = materias(1, 'fisica', 'conceptos', '10 a 12')
materia1.añadirProf(profesor1.nombre)
print(materia1.getMostrarMat())

materia2 = materias(2, 'quimica', 'conceptos', '12 a 2')
materia2.añadirProf(profesor2.nombre)
print(materia2.getMostrarMat())

curso1 = curso(11, 'ciencias', 'lunes y viernes', 'intermedio')
curso1.agregarMat(materia1.nombre)
curso1.agregarMat(materia2.nombre)
curso1.getMostrarCur()