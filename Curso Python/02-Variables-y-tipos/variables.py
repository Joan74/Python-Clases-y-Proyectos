"""
Una variable es un contenedor de infomación
que dentro guardxara un dato, se pueden creaar muchas variables
y que cada una contenga un dato distinto
"""
# Crear Variables y dar un valor

texto = "Curso de:"
texto2 = "Master en Python"
texto3 = "Don quijote"
print("-------------------------------------------")
# mostar valor variables 
print(texto)
print(texto2)
print(texto3)
print("-------------------------------------------")
# Reasignar valores sustituir


numero = 10
decimal = 8,5

print(numero)
print(decimal)
print("-------------------------------------------")


# Concadenación
nombre = "Juan Manuel"
apellidos = "Barrio Sanchez"
web = "Makimania"

print(nombre + " " + apellidos + " - " + web)


print("Hola me llamo {} {} y mi web es: {} ".format(nombre, apellidos,web) )

#Esta esla mejor manera y limpia
print(f"{nombre} {apellidos} - {web}")

print(nombre, apellidos, web)

