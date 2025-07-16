'''Módulo para las funciones donde generamos los números de
ticket según elección y envolverlos entre un par de mensajes.'''


def generate_number(funcion):
    '''Función contenedora para envolver otra función entre dos mensajes.'''
    gen = funcion()
    def shift_number():
        print("\nTu turno es:")
        print(next(shift_number.counter))
        print("Por favor espere su llamado.")
    shift_number.counter = gen
    return shift_number


def perfumeria_num():
    '''Función para obtener el número de ticket de Perfumería del menú principal.'''
    while True:
        for num in range(1,101):
            yield f"P-{num:03d}"

def farmacia_num():
    '''Función para obtener el número de ticket de Farmacia del menú principal.'''
    while True:
        for num in range(1,101):
            yield f"F-{num:03d}"

def cosmeticos_num():
    '''Función para obtener el número de ticket de Cosméticos del menú principal.'''
    while True:
        for num in range(1,101):
            yield f"C-{num:03d}"
