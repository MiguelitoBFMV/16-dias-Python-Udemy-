'''Ejercicio 1
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.


def devolver_distintos(n1, n2, n3):
    lista = [n1, n2, n3]
    if sum(lista) > 15:
        return max(lista)
    elif sum(lista) < 10:
        return min(lista)
    elif 10 <= sum(lista) <= 15:
        lista.sort()
        return lista[1]
    
print(devolver_distintos(2,1,10))



Ejercicio 2
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']

def unique_letters(name):
    name = name.lower()
    letters = []
    for letter in name:
        if letter not in letters:
            letters.append(letter)
    letters.sort()
    return letters


print(unique_letters("Giordano"))


Ejercicio 3
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False

def zero_and_zero(*args):
    numbers= []
    for i in args:
        if i == 0 and numbers[-1] == 0:
            return True
        numbers.append(i)
    return False

print(zero_and_zero(5,6,1,0,0,9,3,5))
print(zero_and_zero(6,0,5,1,0,3,0,1))


Ejercicio 4
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.'''

def contar_primos(number):
    primos = []
    for i in range(0,number + 1):
        if i == 2 or i == 3 or i == 5 or i == 7:
            primos.append(i)
        elif i != 0 and i != 1 and i%i == 0 and i%2 != 0 and i%3 !=0 and i%5 != 0 and i%7 !=0:
            primos.append(i)
    print(primos)
    return f"Se encontraron {len(primos)} números primos"

print(contar_primos(73))