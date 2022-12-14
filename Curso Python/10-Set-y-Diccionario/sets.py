"""
Set es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden.
"""

personas = {
    "Laia",
    "Marga",
    "Arnau",
    "Juanma",
}

personas.add("beto")  # Agregar otra persona
personas.remove("beto")  # Elemina a nombre
print(personas)  # Mostara la lista con el orden que el quiera
print(type(personas))  # mostrara el tipo de dato que es Set
