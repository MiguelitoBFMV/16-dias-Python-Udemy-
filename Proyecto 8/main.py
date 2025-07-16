'''Módulo principal de generación de menú para obtener los tickets llamando al módulo my_numbers.py
y obteniendo sus funciones.'''

import os
from time import sleep
from my_numbers import generate_number, cosmeticos_num,farmacia_num,perfumeria_num

num_p = generate_number(perfumeria_num)
num_f = generate_number(farmacia_num)
num_c = generate_number(cosmeticos_num)

def clean_display():
    '''Limpiar consola'''
    os.system('cls')

def menu():
    '''Menú de selección donde el usuario elige la opción que requiera ejecutar.'''
    election = int(input("\nBienvenido estimado cliente/a\n" \
    "Por favor seleccione al módulo que desea ser atendido:\n" \
    "1. Perfumería\n" \
    "2. Farmacia\n" \
    "3. Cosméticos.\n" \
    "4. Salir.\n" \
    "Su elección: "))
    if election == 1:
        num_p()
        sleep(3)
    elif election == 2:
        num_f()
        sleep(3)
    elif election == 3:
        num_c()
        sleep(3)
    elif election == 4:
        return False
    else:
        print("Su elección es incorrecta, seleccione una opción válida.")
    return True


def main():
    '''Función donde empieza y ejecuta el programa'''
    status_code = True
    while status_code:
        status_code = menu()
        clean_display()


if __name__ == "__main__":
    main()
