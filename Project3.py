'''Proyecto del Día 3
Bueno, el tercer día no ha dejado nada que desear. Hemos visto muchas cosas y de las buenas,
y ha llegado la hora de juntar todo lo aprendido y ponerlo en práctica, creando un programa
perfectamente funcional desde cero.
Ahora que ya sabes usar los métodos y las propiedades de los strings, que sabes indexar
conjuntos de datos como los strings, las listas y los tuples, y sobre todo ahora que conoces
todos los tipos de datos que necesitas para poder almacenar lo que sea, vas a poder encontrar
una forma de programar un analizador de texto.
La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta. '''

lista = input("Ingresa un texto: ").lower()
letters = [input("ingresa un letra: " ).lower() for i in range(3)]

#Print1
l1 = lista.count(letters[0])
l2 = lista.count(letters[1])
l3 = lista.count(letters[2])

print(f"\nLa letra '{letters[0]}' aparece: {l1} veces, la letra '{letters[1]}' aparece: {l2} veces y la letra '{letters[2]}' aparece: {l3} veces")

#Print2

#lista = lista.split()

print(f"Tu texto tiene {len(lista.split())} palabras.")

#Print3

print(lista[0], lista[-1])

#Print4

print(" ".join(lista.split()[::-1]))

#Print5

booleano = False
for i in lista.split():
    if i == "python" or i == "Python":
        booleano = True

print(booleano)