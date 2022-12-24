import os
os.system("clear")
opcion = 0
aciertos = 0
fallos = 0
nombre = input("Introduce tu nombre: ")
print(f"\nComenzamos el test {nombre}")
print("\n                         ---------------------------------------------------------------------")
print("                         ------------------ TEST CIENCIAS VERDADERO O FALSO ------------------")
print("                         ---------------------------------------------------------------------")

print("\n")
print("PULSA 1 VERDADERO")
print("PULSA 2 FALSO")
print()
# PREGUNTAS
preguntas = ["Los electrones son mas pequeños que los atomos ", "Toda la radioactidad es producida por el Hombre ",
             "Los antivioticos curan enfermedades causadas tanto por virus como por bacterias ", "Los seres humanos provienen de especies animales anteriores ",
             "Los rayos laser funcionan mediante la concentracion de ondas de sonido ", "Los continentes se han estado moviendo a lo largo de millones de años y continuarán hacíendolo en el futuro ",
             "El centro de la Tierra está muy caliente ", "El Sol gira alrededor de la Tierra ", "Los primeros humanos vivieron al mismo tiempo que los dinosaurios ",
             "El sol gira alrededor de los planetas"]

for pregunta in preguntas:
    print(f"{preguntas.index(pregunta)+1}. {pregunta}")
print()
# RESPUESTAS
opcion = int(input(f"\nRespuesta pregunta 1: "))
if opcion == 1:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 2: "))
if opcion == 2:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 3: "))
if opcion == 2:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 4: "))
if opcion == 1:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 5: "))
if opcion == 2:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 6: "))
if opcion == 1:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 7: "))
if opcion == 1:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
opcion = int(input(f"Respuesta pregunta 8: "))
if opcion == 2:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 9: "))
if opcion == 2:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
opcion = int(input(f"Respuesta pregunta 10: "))
if opcion == 2:
    print("CORRECTO")
    aciertos += 1
else:
    print("INCORRECTO")
    fallos += 1
print(f"\nPreguntas acertadas : {aciertos}")
print(f"Preguntas falladas : {fallos} ")
if aciertos <= 4:
    print("\n-------------------------------------")
    print(f"      Test SUSPENDIDO {nombre}          ")
    print("-------------------------------------")
else:
    print("\n-------------------------------------")
    print(f"      Test APROBADO  {nombre}          ")
    print("-------------------------------------")
print()
