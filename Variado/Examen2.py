from datetime import datetime  # Mostar fecha y hora
import os
import time  # Importar tiempo
os.system("clear")
print("--------------------------")
now = datetime.now()
print(now)
print("--------------------------")
print()
nombre = input("Introduce tu nombre: ")
print()
print(f"Bienbenido/a {nombre}, Este examen constara de dos preguntas por categorias, COMENZAMOS:")
opcion = 0

while True:
    print("""      
Elige categoria:

1- Naturales
2- Matematicas
3- Ciencia
4- Peliculas
5- Series
6- Salir
""")
    
    opcion = int(input(f"Elige una opción {nombre}: "))
    if opcion == 6:
        os.system("clear")
        exit()
    print()
    acertadas = 0
    falladas = 0
    if opcion == 1:  # NATURALES
        print(" \n         --------- Has elegido Naturales!!!!---------")
        print("\n¿Donde se encuentra España?")  # 1
        print("\n1- EEUU: ")
        print("2- Asia ")
        print("3- Europa ")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 3:
            acertadas +=1
            print(f"\nCORRECTO {nombre}, España esta en EUROPA!!!")
            
        else:
            falladas +=1
            print(f"\nINCORRECTO {nombre}, España esta en EUROPA!!!")

        print("\nLa capital de España es: ")  # 2
        print("\n1- Barcelona ")
        print("2- Madrid ")
        print("3- Andalucia")
        print("4- Pais Vasco")
        opcion = int(input(f"\nElige una opción {nombre}: "))

        if opcion == 2:
            acertadas +=1
            print(f"\nCORRECTO {nombre}, Madrid es la capital de España")
        else:
            falladas +=1
            print(f"\nINCORRECTO {nombre}, Madrid es la capital de España")
        print("\n¿Que es la fotosintesis?")
        print("\n1- Es una fotografia del cuerpo")
        print("2- Es el estudio de las mariposas")
        print("""3- Es el proceso por el cual las plantas verdes y algunos organismos
   usan la luz del sol para trasformar el CO2 y el agua en azucares y oxigeno""")
        print("4- Es la transformacion de la planta a organismo vital")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 3:
            acertadas +=1
            print(f"\nCORRECTO{nombre}, veo que te aprendiste la leccion. ")
        else:
            falladas +=1
            print(f"\nINCORRECTO {nombre}, debes estudiar un poco mas!!!")
        print("\n¿Los ladrillos son de un material hecho por el hombre?")
        print()
        print("1- Si")
        print("2- No")
        print()
        opcion = int(input(f"\nElige una opción {nombre}: "))

        if opcion == 2:
            acertadas +=1
            print(
                f"\nCORRECTO {nombre}, El ingrediente, la Arcilla es natural,pero el ladrillo esta fabricado por el hombre")
        else:
            falladas +=1
            print(f"""\nINCORRECTO Tu si que eres un ladrillo :) {nombre}
   El ingrediente, la Arcilla es natural,pero el ladrillo esta fabricado por el hombre
                  """)
        print("\nPara que sirven los sentidos:")
        print("\n1- Para sobrevivir")
        print("2- Para relacionarnos con el mundo que nos rodea")
        print("3- Para mejorar el rendimiento humano")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            acertadas +=1
            print(
                f"\nCORRECTO {nombre}, sirve para relacionarnos con el mundo que nos rodea ")
        else:
            falladas +=1
            print(
                f"\nINCORRECTO {nombre}, sirve para relacionarnos con el mundo que nos rodea ")
        print("\n¿El sol es un planeta?")
        print("\n1- Verdadero")
        print("2- Falso")

        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            acertadas +=1
            print(f"\nCORRECTO {nombre}, El sol es una Estrella")
        else:
            falladas +=1
            print(f"\nINCORRECTO {nombre}, El sol es una estrella")
            print()
        print("RESULTADO DE PREGUNTAS:")
        print(f"\nPREGUNTAS CORRECTAS: {acertadas}")
        print(f"PREGUNTAS INCORRECTAS: {falladas}")
    elif opcion == 2:  # MATEMATICAS
        print()
        print(f" \n         --------- Has elegido Matematicas !!!!---------")
        print()
        print("La suma de 80 + 174 es:")
        print("-----------------------")
        print()
        print("1- 255")
        print("2- 354")
        print("3- 254")
        print("4- 286")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 3:
            acertadas +=1
            print(f"\nCorrecto {nombre}, El resultado es 254!!!!")
        else:
            falladas +=1
            print(f"\nIncorrecto {nombre}, tienes que repasar la suma, el resultado es 254")
        print()

        print("La multipliacion de 20 x 30 es:")
        print("\n1- 700")
        print("2- 800")
        print("3- 600")
        print("4- 500")
        print()
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 3:
            acertadas +=1
            print(f"\nCorrecto {nombre}, El resultado es 600!!!!!")
        else:
            falladas +=1
            print(f"\nIncorrecto {nombre}, el resultado es 600!!!")
        print("\nRESULTADO DE PREGUNTAS:")
        print(f"\nPREGUNTAS CORRECTAS: {acertadas}")
        print(f"PREGUNTAS INCORRECTAS: {falladas}")
    elif opcion == 3:  # CIENCIA
        print(f"\n         --------- Has elegido Ciencias!!!!---------")
        print()
        print("Cual es el tercer planeta de nuestro sistema solar: ")
        print()
        print("1- Marte")
        print("2- Venus")
        print("3- Tierra")
        print("4- Mercurio")
        print("5- Jupiter")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        print()
        if opcion == 3:
            acertadas +=1
            print(f"Correcto {nombre}, La tierra es el tercer planeta")
        else:
            falladas +=1
            print(f"Incorrecto {nombre}, El tercer planeta es la tierra!!!!")
        print()
        print("¿Ha que distancia se encuentra el espacio sobre el nivel del mar?")
        print()
        print("1- 150 KM")
        print("2- 100 KM")
        print("3- 300 KM")
        print()
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            acertadas +=1
            print(f"\nCorrecto {nombre}, El espacio comienza a 100 km del nivel del mar")
        else:
            falladas +=1
            print(f"\nIncorrecto {nombre}, El espacio comienza a 100 km del nivel del mar")
        print("\n La luna se esta acercando o alejando")
        print("\n1- Acercando")
        print("2- Alejando")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            acertadas +=1
            print(f"\nCorrecto {nombre}, La luna se aleaja 3,78 cm por año")
        else:
            falladas +=1
            print(f"\nIncorrecto {nombre}, La luna se aleaja 3,78 cm por año ")
        print("\nQue es un agujero negro")
        print("\n1- Es un espacio sin universo bagando por el sitema")
        print("""2- Es un cuerpo del espacio de masa grande y poco volumen que absorbe cualquier materia
   o energia situada en su campo de acción""")
        print("3- Es un cuerpo celeste que ocupa los espacios sin materia oscura, ampliando la constelacion")
        print()
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            acertadas +=1
            print(f"\nCorrecto {nombre}, entiendes mucho de astronomia :) ")
        else:
            falladas +=1
            print(f"Incorrecto {nombre}, tienes que estudiar un poco mas, la respuesta correcta es la 2")
        print("\nQue planeta es el mas cercano a nuestra estrella")
        print("\n1- Tierra")
        print("2- Jupiter")
        print("3- Venus")
        print("4- Marte")
        print("5- Urano")
        print("6- Mercurio")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 6:
            acertadas +=1
            print(f"\nCorrecto {nombre}, Mercurio es el mas cercano seguido de Venus")
        else:
            falladas +=1
            print(f"\nIncorrecto {nombre}, Mercurio es el mas cercano seguido de Venus")
        print("\nRESULTADO DE PREGUNTAS:")
        print(f"\nPREGUNTAS CORRECTAS: {acertadas}")
        print(f"PREGUNTAS INCORRECTAS: {falladas}")
    elif opcion == 4:  # PELICULAS
        print(f"\n         --------- Has elegido Peliculas!!!---------")
        print()
        print("Cual es el nombre del actor de BLACK PANTHER:")
        print("\n1- Chadwick Boseman")
        print("2- Michael B. Jordan")
        print("3- Wiston Duke")
        print("4- John Kani")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 1:
            acertadas +=1
            print(f"\nCorrecto {nombre}, El actor es Chadwick Boseman")
        else:
            falladas +=1
            print(f"\nIncorrecto {nombre}, El actor es Chadwick Boseman")

        print("\n¿En cuantas peliculas sale THOR?")
        print("\n1- 3")
        print("2- 4")
        print("3- 8")
        print("4- 10")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        print()
        if opcion == 3:
            acertadas +=1
            print(f"""\nCorrecto {nombre}, sale en:                
Thor
Thor el mundo Oscuro
Thor Ragnarok
Thor Love thunder
Avengers
Avengers Ultron
Avengers Infinity war
Avengers End Game""")
        else:
            falladas +=1
            print(f"""\nIncorrecto {nombre}, Sale en:
Thor
Thor el mundo Oscuro
Thor Ragnarok
Thor Love thunder
Avengers
Avengers Ultron
Avengers Infinity war
Avengers End Game""")
        print("\nRESULTADO DE PREGUNTAS:")
        print(f"\nPREGUNTAS CORRECTAS: {acertadas}")
        print(f"PREGUNTAS INCORRECTAS: {falladas}")
    elif opcion == 5:  # SERIES
        print("\n         --------- Has elegido Series!!!!---------")
        print()
        print("En que serie sale el personaje de Wanda:")
        print("\n1- Loki")
        print("2- Bruja escarlata")
        print("3- Ms Marvel")
        print("4- Hawkeye")
        print("5- Moon knight")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            acertadas +=1
            print(
                f"\nCorrecto {nombre}, Wanda protagonizo La bruja escarlata ")
        else:
            falladas +=1
            print(
                f"\nIncorrecto {nombre}, Wanda protagonizo La bruja escarlata ")
        print("\n En la serie Moon Knight, cuantos personalidades tiene el actor pricipal")
        print("\n1- Marc Spector")
        print("2- Marc Spector + Steven Grant")
        print("3- Super mario + Steven Grant")
        print("4- Steven Grant + Marc Spector + Jake Lockley")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        print()
        if opcion == 4:
            acertadas +=1
            print(f"""CORRECTO {nombre}, Tiene 3 personalidades:
Steven Grant
Marc Spector
Jake Lockley""")
        else:
            falladas +=1
            print(f"""INCORRECTO {nombre}, Tiene 3 personalidades:
Steven Grant
Marc Spector
Jake Lockley""")
        print("\nRESULTADO DE PREGUNTAS:")
        print(f"\nPREGUNTAS CORRECTAS: {acertadas}")
        print(f"PREGUNTAS INCORRECTAS: {falladas}")
