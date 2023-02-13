#pedir un número e imprimir qué día de la semana es, si dijita un número no admitido, usar el except.

def diaSemana():
    try:
        n = int(input('Digite el número: '))
        match n:
            case 1:
                print('Lunes')
            case 2:
                print('Martes')
            case 3:
                print('Miércoles')
            case 4:
                print('Jueves')
            case 5:
                print('Viernes')
            case 6:
                print('Sábado')
            case 7:
                print('Domingo, España vs Alemania --> SIUUUU')
            case _:
                print('Aún no se inventan ese día')
    except ValueError:
        print('El día de la semana no existe')
    except:
        print('error raro')
diaSemana()