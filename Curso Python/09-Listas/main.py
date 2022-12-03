"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice numerico-
"""

pelicula = "Matrix"
# Definir lista
peliculas = ["Matrix", "Reload", "Revolution",
             "Resurrections"]  # Pasar lista (mejor opcion)

actores = list(('Neo', 'Trinity', 'Morpheo'))  # Pasar la lista en tupla
years = list(range(1999, 2022))  # lista con rango de (años)
variada = ["Neo", 1999, True, ]  # Lista variadas

print(peliculas)
print(actores)
print(years)
print(variada)

# Indices

# peliculas[1] = "Lo que el viento se llevo" (Aqui cambiara el dato por el tu quieras)
# en este caso cambaria la pelicula Reload por Loque el viento se llevo
print(peliculas[1]) # Mostrara el indice 1 (empieza por el 0, mostraria reload)
print(peliculas[-2]) # Lo mismo pero al ser negativo empezara a contar desde el final
print(actores[1:3]) # Mostrara el indice del 1 al 3
print(peliculas[0:]) # Mostara apratir del indice 0 y enseñara todos

# Añadir elementos a lista
# .append() añade 
actores.append("Raton")
print(actores)

# Recorrer lista y añadir
print()
nueva_pelicula = ""
while nueva_pelicula != "parar": # Introduciras hasta escribir parar
      nueva_pelicula = input("Introduce la nueva pelicula: ")
      if nueva_pelicula != "parar": # si es igual a parar no mostrar en pantalla
         peliculas.append(nueva_pelicula) # Introduce el indice, 1. etc 2.etc
    
  
print("\n#############LISTADO DE PELICULAS #############")
   
for pelicula in peliculas: # Mostrara el indice en columna
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")
    
