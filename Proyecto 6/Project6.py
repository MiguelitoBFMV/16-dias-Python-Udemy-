'''Proyecto del Día 6
Llegó el momento de poner todo lo que hemos aprendido en un proyecto del mundo real. Y el
de hoy sí que nos va a tomar tiempo, porque a pesar de ser relativamente simple, implica mucho
código, muchas funciones y es imprescindible llevar una especie de orden mental de lo que
necesitas hacer. Hoy vas a crear un administrador de recetas. Básicamente esto es un programa
a través del cual un usuario puede leer, crear y eliminar recetas que se encuentren en una base
de datos.
Entonces, antes de comenzar, es necesario que crees en tu ordenador un directorio en la carpeta
base de tu ordenador, con una carpeta llamada Recetas, que contiene cuatro carpetas y cada
una de ellas contiene dos archivos de texto. Dentro de los archivos puedes escribir lo que
quieras, puede ser la receta en sí misma o no, pero eso no es importante para este ejercicio. Lo
importante es que escribas algo para poder leerlas cuando haga falta o, si prefieres, también
puedes directamente descargar y descomprimir el archivo adjunto a esta elección y ubicarlo en
tu directorio raíz si no tienes ganas de crearlo tú mismo.
Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:
1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
Este programa tiene algunas cuestiones importantes a considerar:
 Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le
va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se
va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo
el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se
cumpla la condición de que la elección del usuario sea 6
 Sería genial que cada vez que el usuario vuelva al menú inicial, la consola limpie la
pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con
system para poder reiniciar la pantalla y comenzar a mostrar todo desde cero.
 Si bien te he enseñado muchos métodos para administrar archivos, para este ejercicio
vas a necesitar algunos que aún no has visto, pero que están incluidos en los objetos con
los que hemos estado trabajando, por lo que en ocasiones deberás buscar entre los
métodos que trae Path, por ejemplo, leer la documentación y aprender a implementarlo.
Yo sé que sería mucho más fácil que yo te enseñe todo acerca de cada uno de los
métodos, pero recuerda que también es importante que a medida que avanzamos vayas
aprendiendo a gestionar tu propio aprendizaje. Es parte de la vida real y cotidiana del
programador en el mundo en que vivimos.
 Utiliza muchas funciones, todas las que creas necesario. Las funciones ayudan a
compartir, mentalizar el código y hacerlo mucho más dinámico, ordenado, repetible y
más fácil de mantener.
 Recuerda comenzar con un diagrama de flujos o un gráfico hecho a mano que te permita
visualizar con más facilidad el árbol de decisiones que necesitas ejecutar en tu código.
Sin eso te vas a enredar más rápido de lo que crees y se te va a complicar bastante.
 Y, por último, no te frustres si no logras hacerlo o completarlo. Si logras hacer una parte,
un par de funciones, algunas cosas sí y otras no, está muy bien. Siempre estamos
aprendiendo y parte de aprender es no saber.
Mis desafíos siempre te van a estar ubicando en el borde de tus capacidades, sacándote del
lugar de confort para que tu cerebro tenga que desconcertarse y descubrir cómo hacer algo
nuevo. Tu avanza hasta donde puedas. '''

import os
from pathlib import Path
HOME = Path.home()
RECIPE_ROUTE = Path(HOME / "Desktop\Proyectos VSCODE\Python Udemy\Materiales de apoyo\Recetas")

def categories():
    return [category.name for category in Path(RECIPE_ROUTE).iterdir() if category.is_dir()]

def recipe_in_file(route):
    return [recipe.stem for recipe in Path(route).iterdir() if recipe.is_file() and recipe.suffix == ".txt"]

def categorie_selected(categories, text):
    print("Estas son las categorías disponibles para ingresar: ", ", ".join(categories))
    categorie = input(text)
    while categorie not in categories:
        categorie = input("Ingresa el nombre exacto de la categoría: ")
    return categorie

def recipe_select(destiny, text):
    category_destiny = Path(RECIPE_ROUTE / destiny)
    recipes_in_file = recipe_in_file(category_destiny)
    if not recipes_in_file:
        return None 
    print(f"\nLas recetas disponibles actualmente en {destiny} son las siguientes:", ", ".join(recipes_in_file))
    recipe_selected = input(f"Ingresa el nombre de la receta a {text}: ")
    while recipe_selected not in recipes_in_file:
        recipe_selected = input(f"Ingresa el nombre correcto de la receta a {text}: ")
    view_recipe = category_destiny / f"{recipe_selected.title()}.txt"
    return view_recipe

def read_recipe(categories):#Option 1
    destiny = categorie_selected(categories, "\nEscribe el nombre de la categoría a la que quieres ingresar: ")
    view_recipe = recipe_select(destiny, "visualizar")
    if view_recipe == None:
        print("\nNo hay recetas!")
    else:
        print(f"El contenido de la receta es: {view_recipe.read_text()}")

def new_recipe(categories):#Option 2
    destiny = categorie_selected(categories, "\nEscribe el nombre de la categoría a la que quieres ingresar: ")
    name_recipe = input("Ingresa el nuevo nombre de la receta a crear: ")
    content_recipe = input("Ingresa el contenido de la receta nueva: ")
    file_selected = Path(RECIPE_ROUTE / destiny / f"{name_recipe}.txt")
    file_selected.write_text(content_recipe)
    print(f"La receta {name_recipe} fue creada con éxito.")

def new_category():#Option 3
    new_file = input("Ingresa el nombre de la nueva categoría que quieres crear: ")
    os.makedirs(RECIPE_ROUTE / new_file)
    print(f"La categoría {new_file} ha sido creada con éxito.")

def delete_recipe(categories):#Option 4
    destiny = categorie_selected(categories, "\nEscribe el nombre de la categoría a la que quieres ingresar: ")
    recipe_deleted = recipe_select(destiny, "eliminar")
    if recipe_deleted == None:
        print("\nNo hay recetas!")
    else:
        recipe_deleted.unlink()
        print(f"La receta {recipe_deleted.stem} ha sido eliminada con éxito.")

def delete_category(categories):#Option 5
    file_delete = categorie_selected(categories, "\nEscribe el nombre de la categoría que quieres eliminar: ")
    while file_delete not in categories:
        file_delete = input("Ingresa un nombre existente: ")
    os.rmdir(RECIPE_ROUTE / file_delete)
    print(f"La categoría {file_delete} ha sido eliminado con éxito.")

def count_all_recipes():
    cont = 0
    for _ in Path(RECIPE_ROUTE).rglob("*.txt"):
        cont += 1
    return cont

def end_code(valor):
    if valor == "Si":
        return True
    else:
        return False

def clear_display():
    return os.system('cls')

def menu():
    print("MENÚ:\n"
    "1. Leer receta por categoría.\n"
    "2. Crear receta por categoría.\n"
    "3. Crear nueva categoría.\n"
    "4. Eliminar receta.\n"
    "5. Eliminar categoría.\n"
    "6. Salir.")
    option = int(input("Por favor, ingresa una de las siguientes opciones: "))
    while option not in range(1,7):
        option = int(input("Ingresa un valor correcto: "))
    if option == 1:
        clear_display()
        read_recipe(categories())
        return True
    elif option == 2:
        clear_display()
        new_recipe(categories())
        return True
    elif option == 3:
        clear_display()
        new_category()
        return True
    elif option == 4:
        clear_display()
        delete_recipe(categories())
        return True
    elif option == 5:
        clear_display()
        delete_category(categories())
        return True
    elif option == 6:
        return False

def main():
    all_recipes = count_all_recipes()
    print("\n¡WELCOME!\n" \
    "\nEste es el Recetario. Aquí podrás gestionar tus recetas que se encuentra en la siguiente ruta:\n" \
    f"{RECIPE_ROUTE}\n" \
    f"Hay en total {all_recipes} recetas entre todas las carpetas.\n")
    status_programm = True
    while status_programm:
        status_programm = menu()
        if status_programm in range(1,6):
            input("\nPresiona Enter para volver al menú...")
        clear_display()


if __name__ == "__main__":
    main()