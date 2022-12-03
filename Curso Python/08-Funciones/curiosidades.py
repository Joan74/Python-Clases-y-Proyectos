""" 
Recomendaciones :
las fuciones es recomendable que esten arriba del todo 
del fichero, y dentro de las funciones utilizar el
return en vez del print.
y hacer el print fuera de la funcion

"""

def mi_funcion(nombre):
    return "Hola que tal " + nombre


def mi_seguna_funcion(apellidos):
    return "Bienbenido Sr. " + apellidos

nombre = "Juan Manuel"
apellidos = "Barrio"

print(mi_funcion(nombre))
print(mi_seguna_funcion(apellidos))
