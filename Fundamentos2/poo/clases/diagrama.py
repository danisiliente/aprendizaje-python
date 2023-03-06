class registrar:
    def __init__(self,documento,nombre,edad,numContac,rol,nombreUsr,contraseña):
        self.__documento = documento
        self.nombre = nombre
        self.edad = edad
        self.telefono = numContac
        self.rol = rol
        self.__username = nombreUsr
        self.__password = contraseña
        self.instructores = []
        self.alumnos = []
        
    def añadir(self):
        if self.rol == 'profesor':
            self.instructores.append({'documento':self.__documento,'rol':self.rol, 'nombre':self.nombre})
        elif self.rol == 'estudiante':
            self.alumnos.append({'documento':self.__documento,'rol':self.rol, 'nombre':self.nombre})
        else:
            print('Rol no admitido.')
        
    def setModificar(self,nombre,edad,numContac,rol,nombreUsr,contraseña):
        self.nombre = nombre
        self.edad = edad
        self.telefono = numContac
        self.rol = rol
        self.__username = nombreUsr
        self.__password = contraseña
        
    def getMostrarI(self):
        return self.instructores
    
    def getMostrarA(self):
        return self.alumnos
    
class instructor(registrar):
    def __ini__(self,credenciales):
        self.credenciales = credenciales
        pass
    
class materias:
    def __init__(self,id,nombre,descripcion,hora):
        self.__id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.hora = hora
        self.materia = []
        
    def agregar (self, instructor):
        self.instructor = instructor
        self.materia.append({'materia':self.nombre,'profesor':instructor.nombre})
        
    def getMostrarM(self):
        return self.materia
        
ins1 = registrar(1234,'Bruno','96','3192998067','profesor','CR7','messi')
ins1.añadir()
print(ins1.getMostrarI())

español = materias(1,'español','lectura','9')
español.agregar(ins1) # Agregación
print(español.getMostrarM())

ins2 = instructor(1004,'Albert','100','3002998022','profesor','messi','CR7')
ins2.añadir()
print(ins2.getMostrarI())

fisica = materias(2,'Física','partículas','12')
fisica.agregar(ins2) # Agregación
print(fisica.getMostrarM())

stu1 = registrar(5678,'Fernando','16','3002998065','estudiante','messi','CR7')
stu1.añadir()
print(stu1.getMostrarA())