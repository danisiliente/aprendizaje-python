# Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula.

def agudas(c):
    c = c.lower()
    tildes = ['á','é','í','ó','ú']
    for i in tildes:
        if c[-1] == i or c[-2] == i and c[-1] == 's' or c[-1] == 'n':
            print('Aguda')
agudas('amor')