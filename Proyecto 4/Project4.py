'''Proyecto del Día 4
A medida que aprendemos a programar, también se incrementa la cantidad de problemas a
los que somos capaces de encontrarle solución gracias al código. Y esto implica que entonces
nuestros desafíos van a ser cada vez más elevados.
Ya sabes usar operadores de comparación, operadores lógicos, hacer control de flujo, hacer
loops, conoces declaraciones muy útiles como random, zip, rango y muchas más. Entonces, ya
estás en condiciones de subir de nivel y que te pida que programes algo un poco más
complicado de lo que hemos hecho hasta ahora. Y hoy vas a crear por primera vez un juego
completamente funcional, con el que podrás divertirte tú mismo un rato.
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos.
¿Te animas? Claro que sí.
Y te recuerdo lo mismo que siempre. Lo importante es que aceptes el desafío. Que te pases un
buen rato intentándolo y puedes lograrlo o no, pero no dejes de darle vueltas al problema.
Cuando quieras, puedes pasar a la lección siguiente con la solución. Yo voy a estar ahí
intentando resolverlo a mi manera, para mostrarte cómo lo haría yo.
Pon buena música, una bebida caliente o fresca, un rincón tranquilo y a programar. '''

from random import randint

name = input("¿Cuál es tu nombre?: ")
trys = 8
print(f"\nBienvenido {name}, al juego de Adivinar el número!\nHe pensado en un número entre 1 y 100.\n"
f"Tienes {trys} intentos para adivinar el número.")
secret_number = randint(1, 100)
print(secret_number)
while trys > 0:
    number_user = int(input("\n¿Qué número eliges?: "))
    if number_user not in range(1, 101):
        print("\nEl número no se encuentra en un rango de 1 a 100. Vuelve a intentarlo.")
    elif number_user < secret_number:
        print("\nNúmero incorrecto! El número elegido es menor al número secreto, intentalo nuevamente.")
        trys -= 1
    elif number_user > secret_number:
        print("\nNúmero incorrecto! El número elegido es mayor al número secreto, intentalo nuevamente.")
        trys -= 1
    else:
        if 8 - trys == 1:
            print(f"\n¡Felicidades! Adivinaste el número con 1 intento.")
            break
        else:
            print(f"\n¡Felicidades! Adivinaste el número con {8 - trys} intentos.")
            break
    print(f"\nTe quedan {trys} intentos.")

if trys == 0:
    print(f"\nLo sentimos, has perdido todos tus intentos. El número secreto era {secret_number}.")


