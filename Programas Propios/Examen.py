import os
print()
os.system("clear")

print("\n")
print("############################ BIENBENIDO/A AL EXAMEN ############################")

print("--------------------------------------------------------------------------------")
print("\n")
print("Total de Preguntas 3:")
nombre = input("¿Cual es tu nombre?: ")
edad = input("Introduce tu edad: ")

print(f"Bienbenida  {nombre} veo que tienes {edad} años:")
print("\n")

print("################################## COMENZAMOS ##################################")
print("--------------------------------------------------------------------------------")


# Variables
pais = 1
continente = 2
localidad = 2
comunidad = 1
santquirze = 1


pais = int(input(
    "PREGUNTA 1: \n¿España es?:\nPulsa 1 Para Pais \nPulsa 2 para Continente:\n\nRespuesta:  "))
print("\n")

if pais == 1:
    print(f"CORRECTO, España es un Pais, FELICIDADES !!!!!!")

elif continente == 2:
    print(f"INCORRECTO, España no es un Continente :(")

print("--------------------------------------------------------------------------------")

comunidad = int(input(
    "PREGUNTA 2:\n¿Catalunya es?:\nPulsa 1 si es una Comunidad\nPulsa 2 si es un Localidad\n\nRespuesta:  "))
print("\n")

if comunidad == 1:
    print(f"CORRECTO, Catalunya es una Comunidad, FELICIDADES !!!!!!!")

elif localidad == 2:
    print(f"INCORRECTO, Catalunya no es un Localidad :(")

print("--------------------------------------------------------------------------------")

print("Pregunta 3:\n")
santquirze = int(input(
    f"¿Sant Quirze del Valles es?:\nPulsa 1 para Municipio\nPulsa 2 para Localidad:\n\nRespuesta:  "))
print("\n")
if santquirze == 1:
    print(f"CORRECTO, Sant Quirze del Valles es un MUNICIPIO.. FELICIDADES!!!!!")
elif localidad == 2:
    print(f"INCORRECTO, Sant Quirze  no es un Localidad :(")

print("--------------------------------------------------------------------------------")
print("\n")
