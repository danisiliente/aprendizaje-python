# Escriba una clase Empleado que tenga como propiedades: nombre, cargo, salario.
# escriba metodos contructores, setters y getters.
# escriba un método que permita calcular cuanto gana el empleado en una hora
# un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 13%
# Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide.
# Contador por cada objeto.

class Empleado:
    contador = 0
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        Empleado.contador += 1
    
    def getAtributos(self):
        return self.__nombre, self.__cargo, self.__salario

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCargo(self, cargo):
        self.__cargo = cargo

    def setSalario(self, salario):
        self.__salario = salario

    def calcSalario(self):
        salario = self.__salario
        self.__salario = salario
        salPorDia = salario // 30
        salPorHora = salPorDia // 8
        return salPorHora

    def incremento(self):
        salario = self.__salario
        if salario > 1160000:
            salario *= 0.13
            print(f'El IPC aumenta en 13% --> {salario}')
        else:
            salario *= 0.16
            print(f'El IPC aumenta en 16% --> {salario}')

    def horasExtra(self, horas):
        salario = self.__salario
        salPorDia = salario // 30
        salPorHora = salPorDia // 24
        if horas <= 40:
            suma = horas * salPorHora
            salario += horas * salPorHora
            print(f'Pago por horas extra = {suma}')
            print(f'Pago de horas extra + salario = {salario}')
        elif horas > 40:
            print('El total de horas no puede ser mayor a 40 horas mensuales.')
        else:
            print('Dato incorrecto.')

ob1 = Empleado('Akiles', 'Scrum Master', 1160000)
print(ob1.getAtributos())
print(ob1.calcSalario())
ob1.incremento()
ob1.horasExtra(1)

ob1.setNombre('Héctor')
print(ob1.getAtributos())