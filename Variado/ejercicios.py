import time
import os
os.system("clear")
si = False
no = True
aciertos = 0
fallos = 0
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print(f"\nEncantado de conocerte {nombre.upper()}")
if edad <= 17:
    print(
        f"Veo que tienes {edad} años, eres menor de edad, te sera un poco dificil pero tienes la suficiente para este test!!!")
else:
    print(
        f"Veo que tienes {edad} años, eres mayor de edad, deberias saber bastantes!!!!!!")
print("\n----------------------------------------")
print("INFORMACION:")
print("PULSA 1 PARA VERDADERO")
print("PULSA 2 PARA FALSO")
print("----------------------------------------")
print("Comenzamos!!!!!!")
time.sleep(8)

os.system("clear")

print("--------------------------------------------------------------------------------------------")
print("                                 TEST DE 10 PREGUNTAS                                       ")
print("--------------------------------------------------------------------------------------------")
respuestas = ["Durante un ataque sorpresa de los daneses a Escocia, uno de los invasores pisó un cardo y emitió un grito de dolor, alertando así a los defensores de su presencia",
                  "Se utilizan 16 fichas como máximo.", "El primero es Rusia.", "Fue un guerrero que unificó a las tribus nómadas mongoles del norte de Asia, fundando el primer Imperio mongol en el siglo XII.",
                  "Es el catalán.", "Fue Camilo José Cela.", "Fue el pueblo Chino quien lo utilizó por primera vez en el siglo I.", "Era Geroge Harrison.",
                  "La Basílica de San Pedro se levanta sobre la que se supone tumba del Apóstol, ubicada en una necrópolis del siglo I y tiene más de 20000 metros cuadrados.",
                  "Dijo  no sé con qué armas se combatirá la Tercera Guerra Mundial, pero la Cuarta será con palos y piedras, en referencia a la aniquilación de la humanidad."]
preguntas = ["Verdadero o falso: Escocia tiene a la flor del cardo por símbolo", "Verdadero o falso: En el parchís tradicional se utilizan 20 fichas como máximo",
                 "Verdadero o falso: Francia es el segundo país más grande de Europa", "Verdadero o falso: Gengis Kan fue un guerrero mongol que se convirtió en emperador de China",
                 "Verdadero o falso: el francés es el idioma oficial de Andorra", "Verdadero o falso: Vicente Aleixandre fue el primer Nobel español que ganó un premio Planeta",
                 "Verdadero o falso: La India fue el primer país en utilizar el papel, lo hicieron cien años después de la muerte de Cristo",
                 "Verdadero o falso: Paul McCartney era el miembro más joven de los Beatles", "Verdadero o falso: el Vaticano es la basílica más grande de la cristiandad",
                 "Verdadero o falso: Albert Einstein dijo que la cuarta guerra mundial se lucharía con piedras"]
for pregunta in preguntas:
        print(f"\n{preguntas.index(pregunta)+1}. {pregunta}")

opcion = int(input("\nIntroduce respuesta pregunta 1: "))
if opcion == 1:
        print("CORRECTO!!!")
        print(respuestas[0])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[0])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 2: "))
if opcion == 2:
        print("CORRECTO!!!")
        print(respuestas[1])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[1])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 3: "))
if opcion == 1:
        print("CORRECTO!!!")
        print(respuestas[2])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[2])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 4: "))
if opcion == 1:
        print("CORRECTO!!!")
        print(respuestas[3])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[3])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 5: "))
if opcion == 2:
        print("CORRECTO!!!")
        print(respuestas[4])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[4])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 6: "))
if opcion == 2:
        print("CORRECTO!!!")
        print(respuestas[5])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[5])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 7: "))
if opcion == 2:
        print("CORRECTO!!!")
        print(respuestas[6])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[6])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 8: "))
if opcion == 2:
        print("CORRECTO!!!")
        print(respuestas[7])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[7])
        fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 9: "))
if opcion == 1:
        print("CORRECTO!!!")
        print(respuestas[8])
        aciertos += 1
else:
    print("INCORRECTO")
    print(respuestas[8])
    fallos += 1
opcion = int(input("\nIntroduce respuesta pregunta 10: "))
if opcion == 1:
        print("CORRECTO!!!")
        print(respuestas[9])
        aciertos += 1
else:
        print("INCORRECTO")
        print(respuestas[9])
        fallos += 1
print("\nTest realizado!!!!!!")
print("\n----------------------------")
print(f"TOTAL DE ACIERTOS; {aciertos}")
print(f"TOTAL DE FALLOS: {fallos}")
print("----------------------------")
