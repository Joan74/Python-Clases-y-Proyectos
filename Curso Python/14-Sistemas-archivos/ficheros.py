from io import open
import pathlib
# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"


archivo = open(ruta, "a+") # crea archivo con permiso de escribir a+
# Escribir dento del fichero
archivo.write("***Soy un texto metido desde python***\n")
archivo.write("***Soy un texto metido desde python***\n")
archivo.write("***Soy un texto metido desde python***\n")
archivo.write("***Soy un texto metido desde python***\n")
archivo.write("***Soy un texto metido desde python***\n")
archivo.write("***Soy un texto metido desde python***\n")
archivo.write("***Soy un texto metido desde python***\n")

# Cerrar archivo

archivo.close()
