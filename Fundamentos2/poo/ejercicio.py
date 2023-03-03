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
        Empleado.contador += 1 # Va aumentando cada vez que se crea o instancia un objeto.
    
    def getAtributos(self):
        return self.__nombre, self.__cargo, self.__salario, Empleado.contador # Retorna al final el número del contador en cada objeto.

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCargo(self, cargo):
        self.__cargo = cargo

    def setSalario(self, salario):
        self.__salario = salario

    def calcSalario(self):
        self.salario = self.__salario # almacena el valor del salario que se le pasa como argumento en el constructor.
        self.salPorDia = self.salario // 30
        self.salPorHora = self.salPorDia // 8 # Suponiendo que trabaja 8 horas diarias.
        return self.salPorHora

    def incremento(self):
        salario = self.__salario
        if salario == 1160000: 
            salario *= 0.16
            print(f'El IPC aumenta en 16% --> {salario}') # Si es el mínimo, aumenta 16% para el siguiente año.
        elif salario > 1160000:
            salario *= 0.13
            print(f'El IPC aumenta en 13% --> {salario}') # Si es más del mínimo, aumenta en 13% para el siguiente año.
        else:
            print('El salario no puede ser menor al mínimo.') # No se puede calcular el IPC si el pago es menos del mínimo.

    def horasExtra(self, horas):
        if horas <= 40:
            suma = horas * self.salPorHora # Se utilizan las variables de calcSalario.
            self.salario += horas * self.salPorHora # Se utilizan las variables de calcSalario.
            print(f'Pago por horas extra = {suma}')
            print(f'Pago de horas extra + salario = {self.salario} \n')
        else:
            print('El total de horas no puede ser mayor a 40 horas mensuales. \n')

ob1 = Empleado('Akiles', 'Diseñador', 1160000)
print(ob1.getAtributos())
print(ob1.calcSalario())
ob1.incremento()
ob1.horasExtra(1)

ob2 = Empleado('Héctor', 'Publicista', 2320000)
print(ob2.getAtributos())
print(ob2.calcSalario())
ob2.incremento()
ob2.horasExtra(40)

ob3 = Empleado('Ajáx', 'Pasante', 580000)
print(ob3.getAtributos())
print(ob3.calcSalario())
ob3.incremento()
ob3.horasExtra(80)