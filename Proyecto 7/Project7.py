import os
from random import randint

class Persona():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

class Cliente(Persona):
    def __init__(self, name, lastname, account_number, balance):
        super().__init__(name, lastname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return(f"Nombre: {self.name} {self.lastname}\n"
              f"N° de Cuenta: {self.account_number}\n"
              f"Su saldo actual es: ${self.balance}")

    def depositar(self):
        status = True
        while status:
            monto = input("\nIngrese la cantidad a depositar: $")
            try:
                monto = int(monto)
                if monto <= 0:
                    print("Ingrese una cantidad mayor a 0.")
                    continue
                status = False
            except ValueError:
                print("Ha ingresado un valor erroneo.\n")
        self.balance += monto
        print(f"\nSe han depositado su dinero exitosamente ${monto}.\n"
              f"Su saldo actual es ${self.balance}.")

    def retirar(self):
        status = True
        while status:
            monto = input("\nIngrese la cantidad a retirar: $")
            try:
                monto = int(monto)
                if monto <= 0:
                    print("Ingrese una cantidad mayor a 0.")
                    continue
                elif monto > self.balance:
                    print("No hay saldo suficiente para realizar esta operación.\n")
                    status = False
                else:
                    self.balance -= monto
                status = False
            except ValueError:
                print("Ha ingresado un valor erroneo.\n")
        print(f"\nSe han retirado su dinero exitosamente ${monto}.\n"
              f"Su saldo actual es ${self.balance}.")

def createClient():
    name = input("\nIngrese su nombre: ")
    lastname = input("Ingrese su apellido: ")
    account = randint(10000, 100000)
    user = Cliente(name, lastname, account, 0)
    return user

def menú(user):
    print(f"\nEstimado/a {user.name} {user.lastname}\n"
          "El menú de opciones es el siguiente: \n"
          "1. Depositar\n" \
          "2. Retirar\n" \
          "3. Salir\n")
    option = int(input("Ingresa una opción: "))
    while option not in range(1,4):
        option = int(input("\nIngrese una opción correcta: "))
    if option == 1:
        user.depositar()
        return True
    elif option == 2:
        if user.balance == 0:
            print("\nNo hay saldo suficiente en la cuenta.")
        else:
            user.retirar()
        return True
    elif option == 3:
        return False

def clear_display():
    os.system('cls')

def main():
    print("\nBienvenido a la gestión de su Cuenta Bancaria!\n"
          "Por favor ingrese los siguientes datos: ")
    user = createClient()
    status = True
    while status:
        input("\n\n\nPresione Enter para continuar...")
        clear_display()
        print(user, "\n")
        status = menú(user)


if __name__ == "__main__":
    main()