class Usuario:
    def __init__(self, documento, nombre, rol, edad, telefono, username, contraseña):
        self.__codumento = documento
        self.nombre = nombre
        self.rol = rol
        self.edad = edad
        self.telefono = telefono
        self.__username = username
        self.__contraseña = contraseña

    def setActualizar(self, edad, telefono, username, contraseña):
        self.edad = edad
        self.telefono = telefono
        self.__username = username
        self.__contraseña = contraseña

    def getMostrar(self):
        print(f'Usuario: {self.nombre} --- Rol: {self.rol}')
#------------------------------------------------------------------------------------
class Profesor(Usuario):
    #var = 'profesor'
    def misMaterias(self):
        pass
#------------------------------------------------------------------------------------
class Estudiante(Usuario):
    #var = 'estudiante'
    def __init__(self):
        self.__codumento = int(input('\nIngrese su documento: '))
        self.nombre = input('Ingrese su nombre: ')
        self.rol = input('Ingrese su rol: ')
        self.icfes = input('Ingrese el código ICFES: ')
        self.edad = input('Ingrese su edad: ')
        self.telefono = input('Ingrese su teléfono: ')
        self.__username = input('Username: ')
        self.__contraseña = input('Defina su contraseña: ')
        self.misCursos = []

    def inscribirse(self, curso):
        self.misCursos.append(curso)
        
    def getMostrarIncripciones(self):
        print(f'{self.nombre}, usted se ecuentra inscrito en el curso ➡  {self.misCursos}')
#------------------------------------------------------------------------------------
class Materia:
    def __init__(self, id, nombre, descripcion, horario):
        self.__id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.horario = horario
#------------------------------------------------------------------------------------
class Curso:
    def __init__(self, id, nombre, descripcion, fecha, nivel):
        self.__id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.nivel = nivel
        self.materias = []
        self.profesores = []

    # COMPOSICIÓN

    def agregarMaterias(self, id, nombre, descripcion, horario):
        self.materia = Materia(id, nombre, descripcion, horario)
        self.materias.append(self.materia.nombre)

    # AGREGACIÓN

    def asignarProfesor(self, profesor):
        self.profesores.append(profesor)

    # COMPOSICIÓN

    def CrearMatricula(self, id, detalles, requerimientos, fecha):
        self.matricula = Inscripcion(id, detalles, requerimientos, fecha)
        print(f'Inscripcion disponible para {self.nombre}')
        print(f'Inscríbase desde {self.matricula.fecha}')
        print(f'Detalles: {self.matricula.detalles}\nRequerimientos: {self.matricula.requerimientos}')

    #GETTERS

    def getMostrarCurso(self):
        print(f'El curso de {self.nombre} está compuesto por ➡  {self.materias}')

    def mostrarProfesores(self):
        print(f'El curso {self.nombre} lo dicta ➡  {self.profesores}' )
#------------------------------------------------------------------------------------
class Inscripcion:
    def __init__(self, id, detalles, requerimientos, fecha):
        self.__id = id
        self.detalles = detalles
        self.requerimientos = requerimientos
        self.fecha = fecha
#------------------------------------------------------------------------------------
usuario1 = Profesor(123, 'Neil', 'Profesor', '30', '322976605', '@Apolo11', '1969')
usuario2 = Profesor(456, 'Shepard', 'Profesor', '33', '300976689', '@Mercury', '1961')

curso = Curso(60, 'Ciencias', 'Relatividad, Estequiometría y Genética', 'Lunes y viernes', 'Nivel Intermedio')
curso.agregarMaterias(1, 'Fisica', 'Relatividad', '8:00 am - 10:00 am') # Composición
curso.agregarMaterias(2, 'Química', 'Estequiometría', '10:00 am - 12:00 md') # Composición
curso.agregarMaterias(3, 'Biología', 'Genética', '12:00 md - 02:00 pm') # Composición
curso.asignarProfesor(usuario1.nombre) # Agregación
curso.asignarProfesor(usuario2.nombre) # Agregación
#------------------------------------------------------------------------------------
# MENÚ
opcion = input('╔══════════╗\n Bienvenido\n╚══════════╝ \n1 - Profesor\n2 - Estudiante\n')
if opcion == '2':
    while opcion != '4':    
        opcion = input('\nEstudiante:\n1 - Ver cursos \n2 - Ver profesores\n3 - Ver inscripciones\n4 - Salir \n')
        match opcion:
            case '1':
                curso.getMostrarCurso()
            case '2':
                curso.mostrarProfesores()
            case '3':
                curso.CrearMatricula(100, 'Disponible', 'Bachiller', '15/03/23 - 22/04/23')
                opcion = input('\n¿Desea Inscribirse al curso?\n1 - Si\n2 - No\n')
                if opcion == '1':
                    estudiante = Estudiante()
                    estudiante.inscribirse(curso.nombre)
                    estudiante.getMostrarIncripciones()
                    break
                else:
                    continue
            case '4':
                print('\n*´¨)\n¸.•´¸.•*´¨) ¸.•*¨)\n(¸.•´ (¸.•` Adiós... 👾 \n')
                break
elif opcion == '1':
    while opcion != '4':
        opcion = input('\nInstructor:\n1 - Cursos asignados \n2 - Materias asignadas\n3 - Crear Curso\n4 - Salir \n')
        match opcion:
            case '1':
                break
            case '2':
                break
            case '3':
                break
            case '4':
                print('\n*´¨)\n¸.•´¸.•*´¨) ¸.•*¨)\n(¸.•´ (¸.•` Adiós... 👾 \n')
                break