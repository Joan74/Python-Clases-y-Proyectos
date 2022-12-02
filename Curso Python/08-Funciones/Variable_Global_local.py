"""
Variables locales:
Se definen dentro de la funcion y no se pueden usar fuera de ella
solo estan disponibles dentro.
A no ser que hagamos return.

Variable Goblal:
Son las que se declaran fuera de una funcion y estan disponibles dentro
y fuera de ellas.

"""

# Variable Global
print()
frase = "a quien buen arbol se arrima, buena sombra le cobija"

print(frase)
# Variable Local


def holaMundo():
    frase = "Hola mundo!!!"
    print("Dentro de la funcion")
    print(frase)

    year = 2022
    print(year)

    global ciudad  # Convierte la variable en global
    ciudad = "Les Fonts"

    return "Dato devuelto " + str(year)# Lo devuelve a global


print(holaMundo())
print("Fuera: ",ciudad)