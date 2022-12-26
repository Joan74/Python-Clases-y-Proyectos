acierto = 0
fallo = 0
opcion = 0
def respues(respuesta):
    if opcion == True:
       print("CORRECTO")
       acierto +=1
    else:
        print("INCORRECTO")
        fallo +=1
        return pregunta
def pregunta():
    return pregunta
print(pregunta, respuesta)

respuesta = int(input("Introduce respuesta: "))







def mostraTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print(f"Tienes {edad} y eres mayor de edad")
    else:
        print(f"Tienes {edad} y eres menor de edad")


nombre = input("Intoduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostraTuNombre(nombre, edad)












preguntas = ["Los electrones son mas pequeños que los atomos ", "Toda la radioactidad es producida por el Hombre ",
             "Los antivioticos curan enfermedades causadas tanto por virus como por bacterias ", "Los seres humanos provienen de especies animales anteriores ",
             "Los rayos laser funcionan mediante la concentracion de ondas de sonido ", "Los continentes se han estado moviendo a lo largo de millones de años y continuarán hacíendolo en el futuro ",
             "El centro de la Tierra está muy caliente ", "El Sol gira alrededor de la Tierra ", "Los primeros humanos vivieron al mismo tiempo que los dinosaurios ",
             "El sol gira alrededor de los planetas"]

for pregunta in preguntas:
    print(f"{preguntas.index(pregunta)+1}. {pregunta}")
print()
